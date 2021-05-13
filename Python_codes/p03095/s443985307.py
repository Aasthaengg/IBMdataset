from collections import Counter


N = int(input())
S = input()


"""
異なる位置から取り出されたものは、同じものがあっても区別する
→各S[i]を入れるか入れないかみたいな話 : 2^N
→たとえば文字aについて、aが複数Sに入っていても、一つしか使えないが、使ったaが異なるなら出来上がりの部分列も区別する
→aを使わないorいずれかのaを一つだけ使う
"""

c = Counter(S)
ans = 1
MOD = 10**9 + 7
for v in c.values():
    ans *= v+1
    ans %= MOD

ans -= 1 # いずれの文字も使わないと空文字になるので
print(ans)
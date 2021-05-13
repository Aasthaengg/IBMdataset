S = list(input())
N = len(S)
num = 0
cnt = [0]*2019
cnt[0] = 1
d = 1
#T[i]: i+1文字目以降を数とみなしたときの数
for i in range(N-1, -1, -1):
    num += int(S[i]) * d
    num %= 2019
    # num = (num + int(S[i]) * 10 ** (N- i -1)) % 2019
    cnt[num] += 1
    d *= 10
    d %= 2019

ans = 0
for c in cnt:
    ans += c * (c-1) // 2
print(ans)
# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d

N = int(input())
S = input()

ans = 0
for i in range(1000):
    key = str(i).zfill(3)
    first = S.find(key[0])
    if first == -1:
        continue
    second = S[first + 1:].find(key[1])
    if second == -1:
        continue
    third = S[first + second + 2:].find(key[2])
    if not third == -1:
        #print(key, first, second, third)
        ans += 1
print(ans)

from math import factorial

n,p = map(int,input().split())
a = list(map(int,input().split()))

cnt = [0,0]
for i in a:
    cnt[i%2] += 1

ans = 0

while True:
    if p > cnt[1]:
        break
    ans += factorial(cnt[1]) // factorial(p) // factorial(cnt[1] - p)
    p += 2

print(ans * 2 ** cnt[0])

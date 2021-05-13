n, p = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0, 0]

for i in a:
    cnt[i % 2] += 1

if cnt[1] == 0:
    print(0 if p == 1 else 2 ** n)
else:
    print(2**(n-1))

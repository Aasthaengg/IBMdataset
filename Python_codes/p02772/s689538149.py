N = int(input())
A = list(map(int,input().split()))

cnt = 0
l = []
for i in A:
    if i % 2 == 0:
        l.append(i)
        cnt += 1

ans = 0
for i in l:
    if i % 3 == 0 or i % 5 == 0:
        ans += 1

if ans == cnt:
    print("APPROVED")
else:
    print("DENIED")
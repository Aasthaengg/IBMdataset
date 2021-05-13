N = int(input())
a = [int(x) for x in input().split()]

cnt = 0
for i in range(N):
    if a[i] % 2 == 0:
        if a[i] % 3 != 0 and a[i] % 5 != 0:
            cnt = 1

if cnt == 1:
    print("DENIED")
else:
    print("APPROVED")
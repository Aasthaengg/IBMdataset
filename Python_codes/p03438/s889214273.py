n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
need1 = 0
need2 = 0
for i in range(n):
    s = B[i]-A[i]
    if s < 0:
        need1 -= s
    else:
        need2 += s//2
if need1 > need2:
    print("No")
else:
    print("Yes")
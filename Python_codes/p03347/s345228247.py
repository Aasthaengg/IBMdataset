N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A.append(0)
if A[0]!=0:
    print(-1)
    exit()
a0 = 0
res = 0
for a in A:
    if a0 >= a:
        res += a0
    elif a - a0 >= 2:
        print(-1)
        exit()
    a0 = a
print(res)
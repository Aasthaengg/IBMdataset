N = int(input())
A = list(map(int, input().split()))
free = 0
color = set()
for i in range(N):
    if A[i]<3200:
        color.add(A[i]//400)
    else:
        free += 1
c = len(color)
if c>0:
    print(c,c+free)
else:
    print(1,free)
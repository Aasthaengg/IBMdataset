n = int(input())
A = list(map(int, input().split()))
B = []
for i in range(n):
    f = True
    for j in range(len(A)):
        if A[len(A)-1-j] == len(A)-j:
            f = False
            B.append(len(A)-j)
            del A[len(A)-j-1]
            break
    if f: break
if len(A) > 0:print(-1)
else: print(*B[::-1], sep="\n")
n = int(input())
A = sorted(list(map(int,input().split())))
for i in range(n):
    if A[i]*2>A[-1]:
        ind = i
        break
ind -= 1
a = A[ind]
b = A[-1]-A[ind+1]
if a>=b:
    print(A[-1],a)
else:
    print(A[-1],A[ind+1])

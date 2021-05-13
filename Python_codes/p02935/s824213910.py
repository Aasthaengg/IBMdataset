N=int(input())
A=list(map(int,input().split()))
A.sort()
for _ in range(N-1):
    t=(A.pop(0)+A.pop(0))/2
    A.insert(0,t)
print(*A)
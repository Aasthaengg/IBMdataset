N = int(input())
A = [int(x) for x in input().split()]

like = []
cnt = 0
for i in range(N):
    if A[A[i]-1] == i+1:
        cnt+=1
print(cnt//2)

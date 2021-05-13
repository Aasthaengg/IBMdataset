N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
sum=0
for i in range(2*N):
    if i%2==1:
        sum+=A[i]

print(sum)


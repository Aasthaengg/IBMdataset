N = int(input())
B = list(map(int, input().split()))
sum=B[0]
for i in range(1,N):
    if i<N-1 and B[i]<=B[i-1]:
        sum=sum+B[i]
    elif i<N-1 and B[i-1]<=B[i]:
        sum=sum+B[i-1]
    else:
        sum=sum+B[N-2]
print(sum)
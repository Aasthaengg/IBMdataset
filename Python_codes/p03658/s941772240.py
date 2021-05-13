N = sorted(map(int, input().split()), reverse=False)
A = sorted(map(int, input().split()), reverse = True)
sum=0
for i in range(0,N[0]):
         sum=sum+int(A[i])
print(sum)
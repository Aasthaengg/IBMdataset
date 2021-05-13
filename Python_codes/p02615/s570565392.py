n=int(input())
A=[]
A=list(map(int, input().split()))

# print(A)
mina = min( A )
maxa = max( A )

A.sort()
A.reverse()

sum = 0
for i in range(n-1):
    sum +=A[(i+1)//2]
    # print(A[(i+1)//2])

# print(mina)
# print(maxa)
# print(sum)
print(sum)

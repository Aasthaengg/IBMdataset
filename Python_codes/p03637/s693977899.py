N=int(input())
*A,=map(int,input().split())

i1=len([i for i in A if i%2!=0])
i4=len([i for i in A if i%4==0])
i2=min(1,N-i1-i4)

# print(i1,i2,i4)
print('Yes' if (i1+i2-1)<=i4 else 'No')
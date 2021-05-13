N=int(input())
*A,=map(int,input().split())

count=0
for a in A:
    count+=1*(a%2==0)

ans=3**N-2**count
print(ans)
n,a,b=map(int,input().split())
ans='Borys' if (b-a+1)%2==0 else 'Alice'
print(ans)
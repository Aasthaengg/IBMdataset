a,b=list(map(int,input().split()))
c=list(input())
d=c[b-1].swapcase()
c[b-1]=d
c=''.join(c)
print(c)
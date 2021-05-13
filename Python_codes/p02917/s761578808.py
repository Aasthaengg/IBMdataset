n=int(input())
b=list(map(int,input().split()))
b.reverse()
ret=min(b[0:1])

for i in range(0,n-1):
  ret+=min(b[i:i+2])

  
print(ret)
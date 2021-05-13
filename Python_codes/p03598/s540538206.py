n=int(input())
k=int(input())
a=list(map(int, input().split()))
l=[]
for i in a:
  r=abs(i-k)
  l.append(min(r,i)*2)
print(sum(l))
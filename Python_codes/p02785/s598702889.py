N,K=map(int,input().split())
I=list(map(int,input().split()))
H=[]
I=sorted(I,reverse=True)
H=I[K:]
s=0
for i in H:
  s+=i
print(s)
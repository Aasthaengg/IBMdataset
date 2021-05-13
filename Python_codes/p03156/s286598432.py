n=int(input())
a,b=map(int,input().split())
P=list(map(int,input().split()))
x=[0]*3
for p in P:
  x[0 if p<=a else (1 if p<=b else 2)]+=1
print(min(x))
n,k=map(int,input().split())
s=input()
x=["a","b","c"]
y=[0]*n
for i in range(n):
  y[i]=s[i]
  if s[k-1]=="A":
    y[k-1]="a"
    
  elif s[k-1]=="B":
    y[k-1]="b"
    
  elif s[k-1]=="C":
    y[k-1]="c"
    

print("".join(y))
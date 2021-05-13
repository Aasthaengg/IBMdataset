p,q,r,s=map(int,input().split())
x=r-p
y=s-q
uy='U'*y
print(uy+'R'*x+'D'*y+'L'*x+'L'+uy+'U'+'R'*(x+1)+'D'+'R'+'D'*(y+1)+'L'*(x+1)+'U')
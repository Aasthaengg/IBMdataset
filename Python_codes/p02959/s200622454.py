f=lambda:map(int,input().split())
input()
p,*A=f()
B=f()
monster = 0
for a,b in zip(A, B):
    t = min(b, p+a)
    p = a - max(0, t-p)
    monster += t
    
print(monster)
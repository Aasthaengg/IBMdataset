n=int(input())
s=list(input())
w=s.count('.')
if s[0]=='.':
    sm=1
else:
    sm=0

def change(y):
    total=(y+1-sm)+(w-sm)
    return total
mn=change(0)
for i in range(1,n):
    if s[i]=='.':
        sm += 1
    mn=min(mn,change(i))
mn=min(mn,w)
print(mn)
X=input()
def split(w):
    return [all for all in w]
before=split(X[0:int(len(X)/2)])
after=split(X[int(len(X)/2):])
c=0
ans=0
reverse=-1
if len(X)%2==1:
    after=after[1:]
for i in after:
    if after[c]!=before[reverse]:
        ans+=1
    c+=1
    reverse-=1
print(ans)
from sys import stdin
moji=(stdin.readline().rstrip())
N=int(stdin.readline().rstrip())
ans=moji[0]
ite=len(moji)
for i in range(1,ite+1):
    if i*N > len(moji)-1:
        break
    ans=ans+moji[i*N]
print(ans)
n=int(input())
def moji(x):
    s=list(x)
    s.sort()
    return "".join(s)
li=[moji(input()) for i in range(n)]
li.sort()
k=1
res=0
for i in range(1,n):
    if li[i]==li[i-1]:
        k+=1
    else:
        res+=k*(k-1)//2
        k=1
res+=k*(k-1)//2
print(res)
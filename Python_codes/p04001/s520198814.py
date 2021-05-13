n=input()
s=len(n)
ans=0
def f(i,cur=""):
    global ans
    #print(i,cur)
    if(i==s):
        ans+=eval(cur)
        return
    f(i+1,cur+n[i])
    if(i!=s-1):f(i+1,cur+n[i]+'+')
f(0)
print(ans)

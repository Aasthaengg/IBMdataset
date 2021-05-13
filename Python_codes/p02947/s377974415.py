def resolve():
    n=int(input())
    s={}
    for i in range(n):
        x=str(sorted(list(input())))
        if x in s.keys():
            s[x]+=1
        else:
            s[x]=1
    ans=0
    if s:
        for i in s.values():
            ans+=i*(i-1)//2
    print(ans)

if __name__ == '__main__':
    resolve()
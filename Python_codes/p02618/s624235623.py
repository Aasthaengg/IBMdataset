def solve(d,c,s,k):
    last=[0]*27
    srate=[]
    ans=[]
    for i in range(1,d+1):
        a=0
        for j in range(1,27):
            a-=c[j-1]*(i-last[j])
        pa=0
        mlast=[0]*2
        for t in range(1,27):
            if s[i-1][t-1]+c[t-1]*(min(k*(k-1)/2,(366-d)*((366-d)-1)/2))>pa:
                mlast=[t,i]
                pa=s[i-1][t-1]+c[t-1]*(i-last[t])
        a+=pa
        last[mlast[0]]=mlast[1]           
        ans.append(mlast[0])
        srate.append(a)
    return [srate[-1]]+ans

def main():
    d=int(input())
    c=list(map(int,input().split()))
    s=[list(map(int,input().split())) for _ in range(d)]
    ans=[]
    for i in range(26):
        ans.append(solve(d,c,s,i))
    ans.sort(reverse=True)
    for i in ans[0][1:]:
        print(i)
    #print(srate[-1])

if __name__ == '__main__':
    main()
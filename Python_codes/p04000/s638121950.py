def sol():
    import sys
    input=sys.stdin.readline
    h,w,n=map(int,input().split())
    d={}
    t=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    for i in range(n):
        y,x=map(int,input().split())
        for a,b in t:
            a+=y
            b+=x
            if 0<a<=h and 0<b<=w and (a,b) in d: d[(a,b)]+=1
            elif 0<a<=h and 0<b<=w: d[(a,b)]=1

    ans=[0]*10
    for i in d:
        if i[0]>2 and i[1]>2:
            ans[d[i]]+=1

    ans[0]=h*w-sum(ans)-w*2-h*2+4
    for i in ans:
        print(i)

if __name__=="__main__":
    sol()
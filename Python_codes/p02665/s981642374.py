n=int(input())
a= list(map(int, input().split()))

# 各階層で可能な点のmin、max
v=[[0,0] for i in range(n+1)]
v[n]=[a[-1],a[-1]]
for i in range(n-1,-1,-1):
    v[i][0]=-(-v[i+1][0]//2)+a[i]
    v[i][1]=v[i+1][1]+a[i]


if v[0][0]>1:
    print(-1)
    exit()

ans=1
# w＝各階層で葉をもつ頂点の個数
w=1
# 各階層でできるだけ多く点をとる。
for i in range(1,n+1):
    w=min(w*2,v[i][1])
    ans+=w
    # 葉っぱは次の階層の根にならない
    w-=a[i]
print(ans)
N,K=map(int,input().split())
ans=0
for b in range(K,N+1):
    if b==0:
        continue
    #aの数
    #N=pb+r
    #0<=r<bをp回ループした後、r個 or r+1個の余りがある
    #(b-K)でK<=r<bを表している
    #(N//b)でループ数を表している
    ans += (b-K)*int(N//b)

    if N%b>=K and K>0:
        #
        ans+=N%b-K+1
    #K=0のときのみ発動
    elif N%b>=K:
        ans+=N%b
print(ans)
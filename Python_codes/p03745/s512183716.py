N = int(input())
src = list(map(int,input().split()))
asc = None
ans=1
for i in range(N-1):
    #隣接項間の差
    d = src[i+1]-src[i]
        #隣接項が等しいとき
    if d==0:
        continue
    #最初または区切った直後のとき
    if asc==None:
        asc = d > 0
        continue
    #隣接項が等しくないとき:
        #ascと隣接項間の差が一致していなければ区切る
    if (asc and d<0) or (not asc and d>0):
        asc = None
        ans+=1
print(ans)
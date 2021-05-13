n = int(input())

dp = [0]*64
#dpの保持変更

#a,g,c =0,1,2
##末尾4文字見る必要がある。3文字ではない

def test(w,x,y,z):
    s = ((0,1,2),(1,0,2),(0,2,1))
    if (x,y,z) not in s and (w,y,z)!=(0,1,2) and (w,x,z)!=(0,1,2):##これ手でノーミスは無理なのだが、処理の実装を思いつく気がしない
        return True
    else:
        return False

for i in range(64):
    x,y,z = i>>4,(i>>2)&3,i&3
    if test(3,x,y,z):
        dp[i]=1

for i in range(3,n):
    dp2 = [0]*64
    for j in range(64):
        w,x,y = j>>4,(j>>2)&3,j&3
        """
        if w not in (0,1,2,3) or x not in (0,1,2,3) or y not in ( 0,1,2,3):
            print(j,w,x,y)
            exit()
        """
        for z in range(4):
            if test(w,x,y,z):
                dp2[(x<<4)+(y<<2)+z]+=dp[j]
    dp = dp2

#for i in range(16):
#    ans+=dp[i][n-1]
ans = sum(dp)
ans%=10**9+7
print(ans)

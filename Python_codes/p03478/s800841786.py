# AtCoder Beginners Selection  Some Sums 解けなかった
N,A,B = map(int,input().split())
ans = 0
for i in range(1,N+1):
    moji = str(str(i).zfill(4))
    sumsomes = int(moji[0])+int(moji[1])+int(moji[2])+int(moji[3])
    if (sumsomes >= A) and (sumsomes <= B):
        ans += i
print(ans)
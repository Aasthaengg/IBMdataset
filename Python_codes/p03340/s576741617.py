N = int(input())
A = list(map(int,input().split()))

nowi = 0
nowj = 0
prej = -1

nowX = 0
nowS = 0
ans = 0

while nowj < N:
    #print(nowS,nowX,0)
    nowS += A[nowj]
    nowX ^= A[nowj]
    if nowX == nowS:
        nowj += 1
    else:
        #print(prej,nowi,nowj,(prej - nowi+1)*(nowj - prej - 1) + (nowj - prej - 1)*(nowj - prej)//2)
        ans += (prej - nowi+1)*(nowj - prej - 1) + (nowj - prej - 1)*(nowj - prej)//2
        prej = nowj - 1
        while nowS != nowX:
            #print(nowS,nowX,1)
            nowS -= A[nowi]
            nowX ^= A[nowi]
            nowi += 1
        nowj += 1
ans += (prej - nowi+1)*(nowj - prej - 1) + (nowj - prej - 1)*(nowj - prej)//2
print(ans)
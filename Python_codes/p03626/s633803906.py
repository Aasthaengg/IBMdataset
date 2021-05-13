n=int(input())
mass=[input()]
mass.append(input())
MOD=10**9+7
if mass[0][0]==mass[1][0]:
    ans=3
    x=0
    y=1
    yoko=False
else:
    ans=6
    x=0
    y=2
    yoko=True
while y<n:
    if x==0:
        if mass[x][y]==mass[x+1][y]:#縦
            yoko=False
            if mass[0][y-1]==mass[1][y-1]:
                ans*=2
                y+=1
            else:
                y+=1
        else:#横
            if yoko:
                ans*=3
            else:
                ans*=2
            yoko=True
            y+=2
print(ans%MOD)

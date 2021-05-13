n=int(input())
syougen=[[] for x in range(n+1)]
for i in range(1,n+1):
    a=int(input())
    for j in range(a):
        x,y=map(int, input().split())
        syougen[i].append([x,y])

ans=0

for katei in range(2**n):
    hantei=katei
    muzyun=False
    for i in range(1,n+1):
        if hantei & 1:
            for j in range(len(syougen[i])):
                taisyou=syougen[i][j][0]
                if katei>>taisyou-1 & 1 != syougen[i][j][1]:
                    muzyun=True
                    break
        hantei>>=1
    if muzyun==False:
        ans=max(bin(katei).count("1"),ans)

print(ans)
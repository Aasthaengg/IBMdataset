ma = lambda :map(int,input().split())
n = int(input())
opens = []
for i in range(n):
    opens.append(list(ma()))
P = []
for i in range(n):
    P.append(list(ma()))

ans = -10**9

for i in range(2**10):
    tmp = 0
    cnts = [0]*n
    if i==0:continue
    for j in range(10):
        if i>>j &1:
            for shop in range(n):
                if opens[shop][j] ==1:
                    cnts[shop]+=1
    for shop in range(n):
        tmp+=P[shop][cnts[shop]]

    ans = max(tmp,ans)
print(ans)

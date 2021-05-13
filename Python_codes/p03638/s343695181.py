H,W = list(map(int,input().split()))
N=input()
a=list(map(int,input().split()))

c=[[0 for j in range(W)] for i in range(H)]
b=[]
for i in range(len(a)):
    b = b + [i+1 for _ in range(a[i])]

f = 0
cnt = 0
for i in range(H):
    f = i % 2
    for j in range(W):
        if f==0:
            c[i][j] = b[cnt]
        else:
            c[i][W-1-j] = b[cnt]
        cnt += 1

        
for i in range(H):
    ans =""

    for j in range(W-1):
        ans += str(c[i][j]) + " " 
    ans += str(c[i][W-1]) 
    print(ans)
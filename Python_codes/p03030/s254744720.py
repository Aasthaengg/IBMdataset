N=int(input())
a=[]
for i in range(N):
    s,p=input().split()
    p=int(p)
    #sortするために数値を逆にする
    a.append((s,-p,i+1))
a.sort()
for i in range(N):
    print(a[i][2])

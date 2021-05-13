H,W=map(int,input().split(' '))
N=int(input())
a=list(map(int,input().split(' ')))
l = []
ans = []
for n,i in enumerate(a):
    for j in range(i):
        l.append(n+1)
for i in range(H):
    tmp = []
    if i%2==0:
        for j in range(W):
           tmp.append(l[i*W+j])
    else:
        for j in range(W-1,-1,-1):
            tmp.append(l[i*W+j])
    ans.append(tmp)
for i in ans:
    for j in i[:-1]:
        print(j,"",end="")
    print(i[-1])
n=int(input())
a=[int(input()) for _ in range(n)]
b=sorted(a)

maxa=max(a)
cnt=0

for aa in a:
    if maxa==aa:
        cnt+=1

if cnt>1:
    for i in range(n):
        print(maxa)
else:
    for aa in a:
        if aa==maxa:
            print(b[-2])
        else:
            print(maxa)
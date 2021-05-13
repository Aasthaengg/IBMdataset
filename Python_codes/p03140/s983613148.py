n=int(input())
s=[list(input()) for _ in range(3)]
cnt=0
for i in range(n):
    l=len(set([s[0][i],s[1][i],s[2][i]]))
    if l==2:
        cnt+=1
    elif l==3:
        cnt+=2
print(cnt)

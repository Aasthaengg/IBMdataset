n=int(input())
d=sorted(map(int,input().split()))
m=int(input())
t=sorted(map(int,input().split()))
cnt=0
for i in range(n):
    if t[cnt]==d[i]:
        cnt+=1
    if cnt>=m:
        print("YES")
        exit()
print("NO")
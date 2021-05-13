n=int(input())
a=sorted(list(map(int,input().split())),reverse=True)

b=a[1::2]
cnt=0
for i in range(n):
    cnt+=b[i]
print(cnt)
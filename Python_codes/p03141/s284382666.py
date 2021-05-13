n=int(input())
AB=[list(map(int,input().split())) for _ in range(n)]

cnt,A=0,[]
for a,b in AB:
    cnt -=b
    A.append(a+b)

A.sort(reverse=True)
for i in range(0,n,2):
    cnt +=A[i]
print(cnt)
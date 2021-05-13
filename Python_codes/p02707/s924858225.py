N=int(input())
*A,=sorted(map(int,input().split()))

s=[0]*N
for i in A:
    s[i-1]+=1
for t in s:
    print(t)
n=int(input())
t,a=map(int,input().split())
h=[int(i) for i in input().split()]
ans=10**10

for i in range(n):
    p=abs(a-(t-h[i]*0.006))
    if p<ans:
        ans=p
        ansnum=i+1

print(ansnum)
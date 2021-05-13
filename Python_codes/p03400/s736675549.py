n=int(input())
d,x=map(int,input().split())
cnt=0
for i in range(n):
    a=int(input())
    cnt+=int(d//a+(d%a)//(d%a-10**(-10)))
print(cnt+x)
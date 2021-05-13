n=int(input())
c=list(map(int, input().split()))
a=b=0
c.sort(reverse=True)
for i in range(n):
    if i%2==0:
        a+=c[i]
    else:
        b+=c[i]

print(abs(a-b))
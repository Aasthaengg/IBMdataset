n=int(input())
s=[]
for _ in range(n):
    x=int(input())
    s.append(x)
sums=sum(s)
if sums%10!=0:
    print(sums)
    exit()
s.sort()
for i in range(n):
    if s[i]%10!=0:
        print(sums-s[i])
        exit()
print(0)
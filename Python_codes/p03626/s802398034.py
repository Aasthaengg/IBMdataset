n = int(input())
a = input()
b = input()
if a[0]==b[0]:
    ans = 3
else:
    ans = 6
l = []
k = 0
while k<n:
    if k==n-1:
        l.append(1)
        k += 1
    elif a[k]==a[k+1]:
        l.append(0)
        k += 2
    else:
        l.append(1)
        k += 1
for i in range(1,len(l)):
    if l[i]==1 and l[i-1]==1:
        ans *= 2
    elif l[i]==0 and l[i-1]==1:
        ans *= 2
    elif l[i]==0 and l[i-1]==0:
        ans *= 3
print((ans)%(10**9+7))
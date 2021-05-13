n = int(input())
a = sorted(list(map(int,input().split())))
cum = [a[0]]
for i in range(1,n):
    cum.append(cum[-1]+a[i])

for i in range(n-2,-1,-1):
    if a[i+1] > cum[i]*2:
        print(n-i-1)
        exit()
print(n)
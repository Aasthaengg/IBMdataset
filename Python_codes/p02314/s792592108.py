n = int(input().split()[0])
c = list(filter(lambda x:x <= n,map(int,input().split())))
m = len(c)

minimum = [n] * (n+1)
minimum[0] = 0
for i in c:
    minimum[i] = 1

for i in range(1,n+1):
    for j in range(m):
        if c[j]<=i and minimum[i-c[j]] + 1 < minimum[i]:
            minimum[i] = minimum[i-c[j]]+1

print(minimum[n])
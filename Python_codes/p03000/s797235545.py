n,x = map(int,input().split())
l = list(map(int,input().split()))

lis = [0]
for i in range(n):
    lis.append(lis[i]+l[i])

print(sum(1 for li in lis if li <= x ))
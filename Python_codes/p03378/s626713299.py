n,m,x = map(int, input().split())
a = list(map(int, input().split()))
m = [0]*n
for i in a:
    m[i-1] += 1
print(min(sum(m[:x-1]), sum(m[x:])))
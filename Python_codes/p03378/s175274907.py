n,m,x = map(int, input().split())
a = list(map(int, input().split()))
l = [0 for l in range(n+1)]
for i in a:
    l[i] = 1
print(min(sum(l[x:]),sum(l[:x])))
from sys import stdin
n,k = map(int,stdin.readline().rstrip().split())
li = list(map(int,stdin.readline().rstrip().split()))
nai = 0
ato = 0
point = 0
for i in range(n):
    for s in range(i+1,n):
        if li[i] > li[s]:
            nai += 1
    for v in range(n):
        if li[i] > li[v]:
            ato += 1
point += (nai*k)+(ato*k*(k-1)//2)
print(point%(10**9+7))

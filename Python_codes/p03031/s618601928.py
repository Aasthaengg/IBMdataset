def solve(Switch, K, P):
    count = 0
    for l_1 in K:
        total = 0
        for i_1 in l_1:
            total += Switch[i_1-1]
        if total % 2 != P[count]:
            return False
        count += 1
    return True

n,m = map(int,input().split())
k = []
for _ in range(m):
    s = list(map(int,input().split()))
    k.append(s[1::])
p = list(map(int,input().split()))

ans = 0

for i in range(2**n):
    switch = [0]*n
    for j in range(n):
        if ((i >> j) &1):
            switch[j] = 1
    if solve(switch, k, p):
        ans+=1

print(ans)
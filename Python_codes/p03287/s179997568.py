from collections import defaultdict

n,m = map(int,input().split())

al = list(map(int,input().split()))

modd = defaultdict(int)

s = 0
for a in al:
    s += a
    s %= m 
    modd[s] += 1
    
ans = 0
for i in modd.values():
    ans += i * (i-1) // 2

ans += modd[0]

print(ans)
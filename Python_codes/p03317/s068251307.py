import math

n,k = map(int,input().split())
s = list(map(int,input().split()))

s.sort()
s.remove(s[0])

ans = math.ceil(len(s)/(k-1))
print(ans)
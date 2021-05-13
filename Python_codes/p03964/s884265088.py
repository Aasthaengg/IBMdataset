N = int(input())
import math
t, a = map(int,input().split())
for i in range(N-1):
    T, A = map(int,input().split())
    g = math.ceil(max(-(-t//T),-(-a//A)))
    t = g*T
    a = g*A
    
ans = t + a
print(ans)
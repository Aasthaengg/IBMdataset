"""abc138_c"""
N = int(input())
V = list(map(int, input().split()))

V_Asc = sorted(V)

ans = 0 
for v in V_Asc:
    ans = (ans + v )/2 if ans != 0 else v
    last = v

print(ans)
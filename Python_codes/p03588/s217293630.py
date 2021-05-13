def I(): return int(input())
def LI(): return list(map(int,input().split()))
N = I()
AB = [LI() for _ in range(N)]
T_AB = list(zip(*AB))
ans = max(T_AB[0])
ans += T_AB[1][T_AB[0].index(max(T_AB[0]))]
print(ans)

N = int(input())
pl = tuple(int(input())for _ in range(N))
p_mx = max(pl)//2
ans = sum(pl) - p_mx
print(ans)
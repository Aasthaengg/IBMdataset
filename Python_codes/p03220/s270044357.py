N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
k = []
for i in range(N):
    t_i = T - H[i] * 0.006
    k.append(abs(t_i-A))
ans = k.index(min(k)) + 1
print(ans)
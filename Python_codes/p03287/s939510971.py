from collections import defaultdict

n, m = map(int, input().split())
A = list(map(int, input().split()))
A_rui = [0, A[0]]
for i in range(1,n):
    A_rui.append(A[i]+A_rui[-1])

A_rui_mod = [x % m for x in A_rui]
mod_m_count = defaultdict(int)

ans = 0
for i in range(n+1):
    mod_m = A_rui_mod[i]
    ans += mod_m_count[mod_m]
    mod_m_count[mod_m] += 1

# print(mod_m_count)
# print(A_rui)
print(ans)
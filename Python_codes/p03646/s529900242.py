import sys
input = sys.stdin.readline

k = int(input())
n = 50
k_m_50 = k % 50
k_q_50 = k // 50

ans = [50]*50
for i in range(k_m_50, 50):
    ans[i] = 49 - k_m_50
for i in range(n):
    ans[i] += k_q_50
print(n)
print(*ans)
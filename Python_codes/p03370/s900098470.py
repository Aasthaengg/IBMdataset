n,x = map(int,input().split())
m_list = [int(input()) for _ in range(n)]

remaining = x - sum(m_list)
print(n + (remaining//min(m_list)))
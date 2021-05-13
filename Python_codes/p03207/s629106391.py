n = int(input())
p = [int(input()) for _ in range(n)]
max_p = max(p)*0.5
print(int(max_p+(sum(p)-max(p))))
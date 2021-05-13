N = int(input())
p = [int(input()) for i in range(N)]
p_max = max(p)
print(sum(p)-p_max//2)
n = int(input())
p = list(map(int, input().split()))
print(sum(max(p[i : i + 3]) != p[i + 1] != min(p[i : i + 3]) for i in range(n - 2)))

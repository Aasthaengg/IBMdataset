n = int(input())
p = list(map(int, input().split()))
print(sum(sorted(p[i:i + 3])[1] == p[i + 1] for i in range(n - 2)))
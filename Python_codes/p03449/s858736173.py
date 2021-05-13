n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
s = [sum(a[0][:i]) + sum(a[1][i-1:]) for i in range(1, n+1)]
print(max(s))
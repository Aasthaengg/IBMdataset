n, l = map(int, input().split())
lst = [l + i for i in range(n)]
m = min(lst, key=lambda x: abs(x))
print(sum(lst) - m)
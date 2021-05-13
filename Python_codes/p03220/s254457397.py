n = int(input())
t, a = map(int, input().split())
lst = list(map(int, input().split()))
print(lst.index(min(lst, key=lambda x: abs(a - (t - x * 0.006)))) + 1)
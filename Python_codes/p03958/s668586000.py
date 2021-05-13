k, t = map(int, input().split())
alst = list(map(int, input().split()))
total = sum(alst)
max_num = max(alst)

print(max(0, max_num * 2 - total - 1))
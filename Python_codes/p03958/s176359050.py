k, t = map(int, input().split())
al = list(map(int, input().split()))

m = max(al)
print(max(0, k-(k-m)*2-1))
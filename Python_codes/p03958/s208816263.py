k, T = map(int, input().split())
t = list(map(int, input().split()))

mt = max(t)

print(max(0, mt-1-(k-mt)))

T = list(map(int, input().split()))

T.remove(max(T))
print(sum(T))

n, k = map(int, input().split())
L = sorted(list(map(int, input().split())), reverse=True)

print(sum(L[0:k]))
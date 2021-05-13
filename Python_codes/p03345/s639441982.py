a, b, c, k = map(int, input().split())
pn = 1 if k%2==0 else -1
print(pn*(a-b))
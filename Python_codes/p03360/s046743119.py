a,b,c = map(int,(input().split()))
K = int(input())
d = max(a,b,c)
for _ in range(K):
    d *= 2
print(a+b+c+d-max(a,b,c))
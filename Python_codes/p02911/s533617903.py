n, k, q = map(int, input().split())
a = [int(input()) for i in range(q)]
c = [0] * n
for ai in a:
    c[ai - 1] += 1
ans = ['Yes' if k - q + ci > 0 else 'No' for ci in c]
print(*ans, sep='\n')
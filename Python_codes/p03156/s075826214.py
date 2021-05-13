n = int(input())
a, b = map(int, input().split())
P = list(map(int, input().split()))

B = [0, 0, 0]

for i in P:
    if i <= a:
        B[0] += 1
    elif i <= b:
        B[1] += 1
    else:
        B[2] += 1
print(min(B))
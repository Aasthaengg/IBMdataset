n = int(input())
B = list(map(int, input().split()))

a = [-1] * n

for i, b in enumerate(B):
    if a[i] > B[i]:
        a[i] = b
        a[i+1] = b
    elif a[i] != -1:
        a[i+1] = b
    elif a[i] == -1:
        a[i] = b
        a[i+1] = b

print(sum(a))
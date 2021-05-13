N = int(input())
A, B = map(int, input().split())
p = list(map(int, input().split()))
a, b, c = 0, 0, 0
for i in p:
    if i <= A: a += 1
    elif i <= B: b += 1
    else: c += 1
print(min(a, b, c))

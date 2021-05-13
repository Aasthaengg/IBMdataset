N = int(input())
A = list(map(int, input().split()))
r = 1
for a in A:
    if a == r:
        r += 1
print(N-r+1 if r != 1 else "-1")

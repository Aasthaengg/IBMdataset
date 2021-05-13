N = int(input())
A = list(map(int, input().split()))
s = 1
for a in A:
    if a%2 == 0:
        s *= 2
ans = 3**N - s
print(ans)
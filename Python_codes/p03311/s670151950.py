N = int(input())
A = list(map(int, input().split()))
B = [a - i for i, a in enumerate(A, 1)]
sorted_B = sorted(B)
b = sorted_B[N // 2]
ans = 0
for i, a in enumerate(A, 1):
    ans += abs(a - (b + i))
print(ans)

N = int(input())
D, X = map(int, input().split())
A = [0] * N
ans = 0
for i in range(N):
    a = int(input())
    A[i] = a
sum = 1
for a in A:
    for i in range(1, 100):
        if 1 + (a * i) > D:
            break
        sum += 1
    ans += sum
    sum = 1
ans += X
print(ans)
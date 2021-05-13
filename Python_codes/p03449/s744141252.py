n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    a_sum = sum(a[:i + 1])
    b_sum = sum(b[i:])
    if ans < a_sum + b_sum:
        ans = a_sum + b_sum

print(ans)
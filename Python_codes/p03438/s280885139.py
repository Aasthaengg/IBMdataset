n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
bigger_a = 0
bigeer_b = 0
for a, b in zip(A, B):
    if a > b:
        bigger_a += a - b
    if b > a:
        bigeer_b += (b - a) // 2
ans = 'Yes' if bigeer_b >= bigger_a else 'No'
print(ans)
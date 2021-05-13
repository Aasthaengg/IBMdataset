N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
score = 0
for a, b in zip(A, B):
    diff = b - a
    if diff > 0:
        score += diff // 2
    else:
        score += diff
print("Yes") if score >= 0 else print("No")

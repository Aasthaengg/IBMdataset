A, B, C = map(int, input().split())
K = int(input())

while K > 0:
    if B <= A:
        B *= 2
    elif C <= B:
        C *= 2
    K -= 1
ans = 'Yes' if A < B < C else 'No'
print(ans)

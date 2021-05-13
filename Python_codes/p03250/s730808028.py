A, B, C = list(input().split())
ans = max(
    int(A) + int(B + C),
    int(A) + int(C + B),
    int(B) + int(A + C),
    int(B) + int(C + A),
    int(C) + int(A + B),
    int(C) + int(B + A))
print(ans)

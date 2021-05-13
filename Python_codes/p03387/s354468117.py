def main():
    A, B, C = map(int, input().split())

    if A == B and A == C:
        return 0

    ans = 0
    sum = A+B+C
    while True:
        sum += 2
        if (sum % 3) == 0 and A<=(sum/3) and B<=(sum/3) and C<=(sum/3):
            break

    m = sum/3
    while True:
        if (m - A) >= 2:
            A += 2
            ans += 1
        else:
            break

    while True:
        if (m - B) >= 2:
            B += 2
            ans += 1
        else:
            break

    while True:
        if (m - C) >= 2:
            C += 2
            ans += 1
        else:
            break

    if A != m or B != m or C != m:
        ans += 1
    return ans

print(main())

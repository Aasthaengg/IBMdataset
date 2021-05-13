def main():
    a = list(map(int, input().split()))
    a.sort()
    A, B, C = a[0], a[1], a[2]
    ans = 0
    ans += C-B
    A = A + ans
    B = B + ans
    ans += (B-A) // 2
    A += ((B-A) // 2) * 2
    if A != B:
        ans += 2
    print(ans)
main()
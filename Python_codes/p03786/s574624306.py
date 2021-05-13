def main():
    n = int(input())
    A = sorted(list(map(int, input().split())))
    B = [A[0], ]
    s = A[0]
    for a in A[1:]:
        s += a
        B.append(s)
    ans = 1
    for i in range(n - 1, 0, -1):
        if B[i - 1] * 2 >= A[i]:
            ans += 1
        else:
            break
    print(ans)
if __name__ == '__main__':
    main()

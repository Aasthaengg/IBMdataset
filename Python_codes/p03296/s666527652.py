def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    ans = 0
    s = A[0]
    count = 0
    for a in A:
        if a == s:
            count += 1
        else:
            s = a
            ans += count // 2
            count = 1
    
    ans += count // 2
    print(ans)

if __name__ == "__main__":
    main()
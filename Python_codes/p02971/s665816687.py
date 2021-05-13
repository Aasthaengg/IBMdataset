def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    sorted_A = sorted(A, reverse=True)
    ans = []
    for a in A:
        if a == sorted_A[0]:
            ans.append(str(sorted_A[1]))
        else:
            ans.append(str(sorted_A[0]))
    print("\n".join(ans))


if __name__ == '__main__':
    main()

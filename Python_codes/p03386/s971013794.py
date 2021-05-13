def main():
    A, B, K = map(int, input().split())
    ans = []
    for v in range(A, min([A+K, B+1])):
        ans.append(v)
    for v in range(max([A, B-K+1]), B+1):
        if v not in ans:
            ans.append(v)
    print("\n".join([str(v) for v in ans]))


if __name__ == '__main__':
    main()

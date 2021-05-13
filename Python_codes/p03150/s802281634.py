def main():
    S = input()
    N = len(S)
    for i in range(N):
        for j in range(i, N+1):
            ans = []
            for k in range(N):
                if i <= k and k < j:
                    continue
                ans.append(S[k])
            if "".join(ans) == "keyence":
                print("YES")
                return
    print("NO")


if __name__ == '__main__':
    main()

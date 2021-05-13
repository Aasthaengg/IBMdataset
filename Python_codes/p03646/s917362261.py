def main():
    K = int(input())
    N = 50
    ans = list(range(50, 0, -1))
    if K <= 50:
        ans = ans[:K] + [0]*(50-K)
    else:
        x = (K-50) // 50
        y = (K-50) % 50
        for i in range(50):
            ans[i] += x
            if i < y:
                ans[i] += 1
    print(N)
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

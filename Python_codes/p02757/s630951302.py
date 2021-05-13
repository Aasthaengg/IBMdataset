from collections import defaultdict

def main():
    n, p = [int(e) for e in input().split()]
    s = input()

    cnt = 0
    if p == 2 or p == 5:
        cum = 0
        for i in range(n - 1, -1, -1):
            if int(s[i]) % p == 0:
                cum += 1

            cnt += cum

    else:
        D = {n: 0}
        exp = 1
        for i in range(n - 1, -1, -1):
            D[i] = (D[i + 1] + (int(s[i]) * exp % p)) % p
            exp *= 10
            exp %= p

        Di = defaultdict(int)
        Di[0] = 1
        for i in range(n - 1, -1, -1):
            Di[D[i]] += 1
            cnt += Di[D[i]] - 1

    print(cnt)

if __name__ == "__main__":
    main()

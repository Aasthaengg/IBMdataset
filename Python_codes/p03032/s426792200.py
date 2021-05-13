def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    reversed_v = [0] + v[::-1]
    v = [0] + v
    ans = -float("inf")
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j > min(n, k):
                continue
            now_k = k - i - j
            if now_k < 0:
                continue
            q = []
            for l in range(1, i + 1):
                q.append(v[l])
            for l in range(1, j + 1):
                q.append(reversed_v[l])
            q.sort()
            for l in range(len(q)):
                if q[l] < 0 and now_k > 0:
                    q[l] = 0
                    now_k -= 1
            ans = max(ans, sum(q))
    print(ans)


if __name__ == '__main__':
    main()

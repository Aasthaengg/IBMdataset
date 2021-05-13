
def main():
    N = int(input())
    L = list(map(int, input().split(" ")))
    cnt = 0
    for i in range(N-2):
        for j in range(i + 1, N-1):
            for k in range(j + 1, N):
                l1 = L[i]
                l2 = L[j]
                l3 = L[k]
                l_max = max(l1, l2, l3)
                if l1 == l2 or l2 == l3 or l3 == l1:
                    continue
                if (l1+l2+l3) - l_max <= l_max:
                    continue
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
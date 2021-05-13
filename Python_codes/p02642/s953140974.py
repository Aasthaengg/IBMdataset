# review
def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    OK = [True for i in range(10**6+1)]
    CNT = [0 for i in range(10**6+1)]
    for x in A:
        CNT[x] += 1
        if CNT[x] == 1:
            for i in range(2, 10**6+1):
                if i*x > 10**6:
                    break
                OK[i*x] = False
    for x in A:
        if CNT[x] == 1 and OK[x]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
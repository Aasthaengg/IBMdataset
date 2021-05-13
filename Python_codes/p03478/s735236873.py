def main():
    N, A, B = map(int, input().split())
    ans = 0
    for i in range(N+1):
        tw = str(i)
        tn = 0
        for j in range(len(tw)):
            tn += int(tw[j])
        if A <= tn <= B:
            ans += i
    print(ans)
main()
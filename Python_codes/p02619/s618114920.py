def main():
    d = int(input())

    c =list(map(int, input().split()))

    s = [[] for i in range(d)]
    for i in range(d):
        s[i] = list(map(int, input().split()))

    t = [0 for i in range(d)]
    for i in range(d):
        t[i] = int(input())

    ans = 0
    last = [0 for i in range(26)]

        
    for i in range(d):
        ans += s[i][t[i]-1]
        last[t[i]-1] = i+1

        sum_ = 0
        for j in range(26):
            sum_ += c[j] * (i+1-last[j])

        ans -= sum_
        print(ans)
        
main()

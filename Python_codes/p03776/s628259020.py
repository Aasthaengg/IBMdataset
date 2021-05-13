import sys
input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())
    v = sorted(list(map(int, input().split())), reverse=True)

    kai = [1] * (N+1)

    for i in range(1, N+1):
        kai[i] = i * kai[i-1]

    ans1 = sum(v[:A]) / A

    dic = {}
    for t in v:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
    
    dic = sorted(dic.items(), reverse=True)
    # print(dic)
    tmp = 0
    for i in range(N):
        tmp += dic[i][1]
        if tmp >= A:
            ind = i
            must = A - (tmp - dic[i][1])
            max_ = min(B, tmp) - (tmp - dic[i][1])
            break
    n = dic[ind][1]
    if ind == 0:
        ans2 = 0
        # nCA ~ nCmax_
        for i in range(A, max_+1):
            ans2 += (kai[n] // kai[n - i]) // kai[i]
    else:
        # nCmust
        ans2 = (kai[n] // kai[n - must]) // kai[must]
    
    print(ans1)
    print(ans2)

if __name__ == "__main__":
    main()
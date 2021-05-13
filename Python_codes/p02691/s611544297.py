def main():
    n = int(input())
    a = list(map(int, input().split()))
    plus = [None]*n
    minus = [None]*n
    for i, ai in enumerate(a, 1):
        plus[i-1] = i+ai
        minus[i-1] = i-ai
    plus.sort()
    minus.sort()
    ans = 0
    j = 0
    i = 0
    while i < n:
        pi = plus[i]
        p_num = 1
        m_num = 1
        while j < n-1 and minus[j] < pi:
            j += 1
        mi = minus[j]
        if mi == pi:
            while j < n-1 and mi == minus[j+1]:
                m_num += 1
                j += 1
            while i < n-1 and pi == plus[i+1]:
                p_num += 1
                i += 1
            ans += p_num*m_num
        i += 1
        
    print(ans)
    

if __name__ == "__main__":
    main()
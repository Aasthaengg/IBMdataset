def solve():
    S = input()
    K = int(input())

    N = len(S)

    st = set()

    for left in range(N):
        for right in range(left+1,N+1):
            if right - left > K:
                break
            st.add(S[left:right])
    
    tmp = list(st)
    tmp.sort()
    print(tmp[K-1])

if __name__ == '__main__':
    solve()
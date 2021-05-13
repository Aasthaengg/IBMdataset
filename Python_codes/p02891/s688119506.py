def mi():
    return map(int, input().split())

def main():
    S = input()
    K = int(input())
    N = len(S)
    if len(set(S)) == 1:
        print(N*K//2)
    else:
        SS = S+S
        t = ''
        tt = ''
        flg = 0
        for i in range(N):
            if i and t[i-1] == S[i]:
                t += '#'
            else:
                t += S[i]

        for i in range(2*N):
            if i and tt[i-1] == SS[i]:
                tt += '#'
            else:
                tt += SS[i]

        d = tt.count('#')-t.count('#')
        print(t.count('#')+(K-1)*d)

if __name__ == '__main__':
    main()

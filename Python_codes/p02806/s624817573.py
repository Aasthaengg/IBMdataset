def main():
    N = int(input())
    S,T = [],[]
    for _ in range(N):
        s,t = map(str,input().split())
        t = int(t)
        S.append(s)
        T.append(t)
    X = input()
    T_cumsum = [T[0]]
    for i in range(1,N):
        T_cumsum.append(T_cumsum[-1]+T[i])
    
    for i in range(N):
        if S[i]==X:
            idx = i
            break
    
    print(sum(T)-T_cumsum[i])

if __name__ == '__main__':
    main()
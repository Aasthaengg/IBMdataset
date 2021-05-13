def main():
    N, A, B, C, D = map(int, input().split())
    S = list(input())
    E = max(C, D)
    cnt = 0
    for i in range(A-1, E):
        if S[i] == '#':
            cnt += 1
        else:
            cnt = 0
        if cnt >= 2:
            print('No')
            return
    if C < D:
        print('Yes')
        return
    cnt = 0
    for i in range(B-2, D+1):
        if S[i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            print('Yes')
            return
    print('No')
        
if __name__ == "__main__":
    main()

def main():
    N, M, K = (int(_) for _ in input().split())
    for a in range(N+1):
        for b in range(M+1):
            if b*(N-a)+a*(M-b) == K:
                print('Yes')
                break
        else:
            continue
        break
    else: print('No')
    return

if __name__ == '__main__':
    main()

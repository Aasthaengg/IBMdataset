def main():    
    N, M = map(int, input().split())
    S = input()
    p = N
    a = []
    while p > 0:
        for i in range(min(M, p), 0, -1):
            if S[p - i] == '0':
                p = p - i
                a.append(str(i))
                break
        else:
            return -1
    return ' '.join(i for i in reversed(a))
print(main())

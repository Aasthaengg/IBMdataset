from collections import deque

def main():
    N,K,C = map(int, input().split())
    S = input()

    f = [-1 for i in range(K+1)]
    b = [-1 for i in range(K+1)]

    count = 0
    i = 0
    while i < N and count < K:
        if S[i] == 'o':
            count += 1
            f[count] = i
            i += C+1
        else:
            i += 1
    
    count = K
    j = N-1
    while j >= 0 and count > 0:
        if S[j] == 'o':
            b[count] = j
            count -= 1
            j -= C+1
        else:
            j -= 1

    i = 0
    j = N-1

    for i in range(1,K+1):
        if f[i] != -1 and f[i] == b[i]:
            print(f[i]+1)


main()
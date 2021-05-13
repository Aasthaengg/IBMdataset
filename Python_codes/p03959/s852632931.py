#! /usr/bin/env python3

def main():
    ans = 1
    D = 10 ** 9 + 7
    N = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))
    L = len(T)
    ST, SA = [0] * L, [0] * L
    ST[0], SA[-1] = T[0], A[-1]
    if L > 1:
        if T[-1] != T[-2] : ST[-1] = T[-1]
        if A[0] != A[1] : SA[0] = A[0]
    for i in range(1, L-1):
        if T[i] == T[i-1] and A[i] == A[i+1]:
            ans = (ans * min(T[i], A[i])) % D
        else:
            if T[i] != T[i-1] : ST[i] = T[i]
            if A[i] != A[i+1] : SA[i] = A[i]
    for i in range(L):
        if ST[i] and SA[i] and ST[i] != SA[i]:
            ans = 0; break
        if A[i] < ST[i] or T[i] < SA[i]:
            ans = 0; break
    print(ans)
    
if __name__ == '__main__':
    main()
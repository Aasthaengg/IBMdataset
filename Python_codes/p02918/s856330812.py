#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N, K = map(int, input().split())
    S = input()
    ret = 0
    for i in range(1,N-1):
        if (S[i]=='L' and S[i-1]=='L') or (S[i]=='R' and S[i+1]=='R'):
            ret += 1
    if S[0]=='R' and S[1]=='R':
        ret += 1
    if S[N-1]=='L' and S[N-2]=='L':
        ret += 1

    print(min(N-1,ret+2*K))

if __name__ == '__main__':
    main()
#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    al = set(list('abcdefghijklmnopqrstuvwxyz'))
    S = input()
    if S == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
    elif len(S)==26:
        for i in range(len(S)-1,-1,-1):
            for x in sorted(list(S[i:])):
                if x > S[i-1]:
                    print(S[:i-1]+x)
                    exit()

    else:
        for i in S:
            al-=set(i)
        al = sorted(list(al))
        print(S+al[0])

if __name__ == '__main__':
    main()
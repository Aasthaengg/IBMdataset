#!/usr/bin/env python3

def solve(s):
    ans = 0
    one = False
    i = 0
    n = len(s)

    while i < n:
        if i == n - 2 and  s[i] == s[i+1]:
            ans += 1
            break
        elif one and s[i] == s[i-1]:
            ans += 1
            i += 2
            one = False
        else:
            ans += 1
            i += 1
            one= True 

    return ans



def main():
    S = input()
    print(solve(S))
    return

if __name__ == '__main__':
    main()

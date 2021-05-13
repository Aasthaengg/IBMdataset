#!/usr/bin/env python3

def main():
    a,b,k = map(int,input().split())
    s = list(set(range(a,min(a+k,b+1))) | set(range(max(b-k+1,a),b+1)))
    s = sorted(s)

    for i in range(len(s)):
        print(s[i])


if __name__ == '__main__':
    main()
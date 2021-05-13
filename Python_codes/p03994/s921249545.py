def main():
    import sys
    from collections import defaultdict

    def input(): return sys.stdin.readline().rstrip()

    s = input()
    n = len(s)
    k = int(input())
    for i in range(n):
        tmp = (ord('a')-ord(s[i]))%26
        if tmp > k:
            continue
        k -= tmp
        s = s[:i]+'a'+s[i+1:]
    s = s[:-1]+chr((ord(s[-1])+k%26-ord('a'))%26+ord('a'))
    print(s)

    
if __name__ == '__main__':
    main()
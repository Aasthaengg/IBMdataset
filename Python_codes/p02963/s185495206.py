def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    s = int(input())
    i = int(s**0.5)
    while i*i < s:
        i+= 1
    r = i*i-s
    ans = [0, 0, i, r, 1, i]
    print(*ans)
        
        
if __name__ == '__main__':
    main()
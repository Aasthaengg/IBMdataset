def main():
    import sys
    input = sys.stdin.readline
    s = list(input().strip())
    K = int(input())
    for i, c in enumerate(s):
        if c == 'a':
            continue
        z = 123 - ord(c)
        if K >= z:
            s[i] = 'a'
            K -= z
        if K == 0:
            break
    
    s[-1] = chr(((ord(s[-1])-97+K))%26+97)

    print(''.join(s))

if __name__ == '__main__':
     main()
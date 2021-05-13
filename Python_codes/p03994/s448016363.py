import sys
#input = sys.stdin.buffer.readline

def main():
    s = list(input())
    K = int(input())
    
    l = len(s)
    for i in range(l-1):
        moji = s[i]
        if moji == "a":
            continue
        else:
            a = ord("z")-ord(moji)+1
            if a <= K:
                s[i] = "a"
                K -= a

    K %= 26
    use = ord(s[-1])+K
    if use >= 123:
        use -= 26
    s[-1] = chr(use)
    print("".join(map(str,s)))
    
if __name__ == "__main__":
    main()
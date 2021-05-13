def main():
    import sys
    input = sys.stdin.readline
    S = input().strip()
    if len(S) < 26:
        for i in range(97, 123):
            if chr(i) not in S:
                print(S + chr(i))
                return
    
    p = 0
    q = []
    for i, s in enumerate(S[::-1]):
        if ord(s) > p:
            p = ord(s)
            q.append(ord(s))
        else:
            min_ = 123
            for j in q:
                if j > ord(s):
                    min_ = min(min_, j)
            print(S[:-i-1] + chr(min_))
            return
    print('-1')

if __name__ == '__main__':
    main()
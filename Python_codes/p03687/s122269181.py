def main():
    import sys
    input = sys.stdin.readline
    s = list(input().strip())

    def solve(c, s):
        if c not in s:
            return float('inf')
        ret = 0
        while s != [c] * len(s):
            f = True
            ret += 1
            s_ = [''] * (len(s)-1)
            for i in range(len(s)-1):
                if s[i] == c or s[i+1] == c:
                    s_[i] = c
                else:
                    s_[i] = s[i]
                    f = False
            s = s_[:]
            if f:
                break
        
        return ret
        
    ret = float('inf')
    for c in 'abcdefghijklmnopqrstuvwxyz':
        ret = min(ret, solve(c, s[:]))

    print(ret)

if __name__ == '__main__':
    main()
def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    s_table = [0]*3
    ans = 0
    for i in range(n):
        s = input()
        ans += s.count('AB')
        if s[0] == 'B' and s[-1] == 'A':
            s_table[0] += 1
        elif s[0] == 'B' and s[-1] != 'A':
            s_table[1] += 1
        elif s[0] != 'B' and s[-1] == 'A':
            s_table[2] += 1
    
    if s_table[0] == 0:
        ans += min(s_table[1:])
    elif sum(s_table[1:]) > 0:
        ans += s_table[0]+min(s_table[1:])
    else:
        ans += s_table[0]-1
    print(ans)
        
    
if __name__ == '__main__':
    main()
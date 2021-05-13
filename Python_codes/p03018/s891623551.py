
        
def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    s = input()
    s = s.replace('BC', 'D')
    n = len(s)
    i = 0
    ans = 0
    while i < n:
        while i < n and (s[i] == 'B' or s[i]=='C'):
            i += 1
        st = i
        cnt = 0
        while i < n and (s[i] == 'A' or s[i]=='D'):
            if s[i] == 'A':
                cnt += 1
            i += 1
        ed = i
        for j in range(st, ed):
            if s[j] == 'A':
                cnt -= 1
                ans +=ed-j-cnt-1
    print(ans)

    
    


                
if __name__ == '__main__':
    main()
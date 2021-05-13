def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    s = input()
    t = input()
    for i in range(len(s)):
        if s.index(s[i]) != t.index(t[i]):
            print('No')
            return
    print('Yes')
        
        
        
            
        
    
    
if __name__ == '__main__':
    main()
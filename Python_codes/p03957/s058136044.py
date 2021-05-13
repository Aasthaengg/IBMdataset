import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        s=list(input())
        ls=len(s)
        for i in range(ls-1):
            for j in range(i+1,ls):
                if s[i]=='C' and s[j]=='F':
                    return 'Yes'
        return 'No'
    print(main())
    
resolve()
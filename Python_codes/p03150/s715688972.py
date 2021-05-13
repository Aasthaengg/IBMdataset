import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():

        s=input()
        n=len(s)
        if s=='keyence':
            return 'YES'
        else:
            for i in range(n):
                for j in range(i+1,n+1):
                    if s[:i]+s[j:]=='keyence':
                        return 'YES'
            return 'NO'
    print(main())
resolve()
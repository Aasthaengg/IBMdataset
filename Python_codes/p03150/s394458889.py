import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        S=str(input())
        ls=len(S)

        if S=='keyence':
            return 'YES'
        else:



            for i in range(ls):
                for j in range(i+1,ls):
                    if S[:i]+S[j:]=='keyence':
                        return 'YES'
            return 'NO'
    print(main())



resolve()
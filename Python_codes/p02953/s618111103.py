import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        n=int(input())
        H=list(map(int,input().split()))
        H.reverse()
        val=H[0]
        for i in range(1,n):
            if val>=H[i]:
                val=H[i]
            elif val==H[i]:
                continue
            elif H[i]-val==1:
                continue
            else: return 'No'
        return 'Yes'
    print(main())

    
resolve()
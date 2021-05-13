import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        x,a,b=map(int,input().split())
        if a>=b: return 'delicious'
        elif b-a<=x: return 'safe'
        else: return 'dangerous'
    print(main())

    
resolve()
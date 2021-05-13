import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():

        n=int(input())
        d=list(map(int,input().split()))
        m=int(input())
        t=list(map(int,input().split()))
        from collections import Counter
        dd=Counter(d)
        tt=Counter(t)
        for key,value in tt.items():
            if dd[key]<value:
                return 'NO'
        return 'YES'
    print(main())
resolve()
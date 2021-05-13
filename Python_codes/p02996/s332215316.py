import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():

        n=int(input())
        l=[list(map(int,input().split())) for i in range(n)]
        l.sort(key=lambda x:x[1])
        time=0
        for x,y in l:
            time+=x
            if time>y:
                return 'No'
        return 'Yes'
    print(main())

resolve()
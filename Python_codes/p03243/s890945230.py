import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        n=int(input())
        x=999-n
        if str(n)[0]==str(n)[1]==str(n)[2]:
            return n
        for i in range(x+1):
            n+=1
            if str(n)[0]==str(n)[1]==str(n)[2]:
                return n
    print(main())
resolve()
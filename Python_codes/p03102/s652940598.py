import sys
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def Main():
    n,m,c = IL()
    b = list(IL())
    ans = 0
    for _ in range(n):
        a = list(IL())
        tmp = 0
        for i in range(m):
            tmp += b[i]*a[i]
        if -c<tmp: ans += 1
    print(ans)
    return

if __name__=='__main__':
    Main()
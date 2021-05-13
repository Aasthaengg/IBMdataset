import sys
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def Main():
    n,x,y = IL()
    x -= 1
    y -= 1
    dist = [0]*(n-1)
    for i in range(n):
        for j in range(i+1,n):
            dist[min(abs(j-i),abs(j-x)+abs(x-i),abs(y-j)+abs(x-i)+1)-1] += 1
    for rep in dist:
        print(rep)
    return

if __name__=='__main__':
    Main()
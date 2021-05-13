import sys
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def Main():
    n = I()
    p = list(IL())
    q = sorted(p)
    flag = 3
    for i in range(n):
        if p[i] != q[i]:
            flag -= 1
        if not flag:
            print("NO")
            exit()
    print("YES")
    return

if __name__=='__main__':
    Main()
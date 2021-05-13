import sys
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def Main():
    n,m = IL()
    war = [list(IL()) for _ in range(m)]
    war.sort(key=lambda x: x[1])
    pre = war[0][1]-2
    ans = 1
    for rep in war:
        if pre<rep[0]-1:
            pre = rep[1]-2
            ans += 1
    print(ans)
    return

if __name__=='__main__':
    Main()
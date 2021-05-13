import sys
import itertools
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def Main():
    n,x = IL()
    l = [0]+list(IL())
    l = list(itertools.accumulate(l))
    ans = 0
    for rep in l:
        if x<rep:   break
        ans += 1
    print(ans)
    return

if __name__=='__main__':
    Main()
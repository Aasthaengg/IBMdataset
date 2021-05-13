import sys
from collections import Counter
def input(): return sys.stdin.readline().rstrip()


def main():
    n=int(input())
    wlist=[]
    for _ in range(n):
        n=input()
        n=list(n)
        n.sort()
        n=''.join(n)
        wlist.append(n)
    cnt=Counter(wlist)
    ans=0
    for c in cnt.values():
        ans+=c*(c-1)//2
    print(ans)

if __name__ == '__main__':
    main()
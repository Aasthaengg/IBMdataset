import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=list(map(int,input().split()))
    cnt=0
    for i in l:
        if i%2==1:
            cnt+=1
    if cnt%2==1:
        print('NO')
    else:
        print('YES')
resolve()
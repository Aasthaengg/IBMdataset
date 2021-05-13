import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    cnt=0
    n=input()
    for i in n:
        if i=='2':
            cnt+=1
    print(cnt)
resolve()
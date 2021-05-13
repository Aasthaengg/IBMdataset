import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    t='CODEFESTIVAL2016'
    cnt=0
    for ss,tt in zip(s,t):
        if ss!=tt:
            cnt+=1
    print(cnt)
resolve()
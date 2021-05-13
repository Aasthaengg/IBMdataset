import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    t=input()
    cnt=0
    for i in range(3):
        if s[i]==t[i]:
            cnt+=1
    print(cnt)
resolve()
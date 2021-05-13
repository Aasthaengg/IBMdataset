import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    cnt=0
    prev=''
    ima=''
    for i in s:
        ima+=i
        if ima!=prev:
            cnt+=1
            prev=ima
            ima=''
    print(cnt)
resolve()
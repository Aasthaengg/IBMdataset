import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    s=str(input())
    ls=len(s)
    cnt=1
    i=1
    temp=1
    while True:
        if i==ls:
            break
        if temp==2:
            cnt+=1
            temp=1
            i+=1
        else:
            if s[i-1]!=s[i]:
                i+=1
                cnt+=1
                temp=1
            else:
                if i==ls-1:
                    break
                else:
                    i+=2
                    cnt+=1
                    temp=2
    print(cnt)
resolve()
import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    k=int(input())
    ans=1
    # k文字目までずっと１だったらans=1
    # そうじゃないなら1以外の数で最初に出てくるやつがans
    for i in range(k):
        if s[i]!='1':
            ans=s[i]
            break
    print(ans)
resolve()
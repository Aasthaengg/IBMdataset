import sys
def S(): return sys.stdin.readline().rstrip()

if __name__=='__main__':
    sl = list(S())
    ans = 0
    c = 0
    for i,item in enumerate(sl):
        if item=='W':
            ans += c
        else:
            c += 1

    print(ans)
    exit()
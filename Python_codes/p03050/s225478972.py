import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    N=int(input())
    cnt=0
    i=1
    while True:
        M=N
        M-=i
        p=M/i
        if p<=i:
            break
        else:
            if p.is_integer():
                cnt+=p
            i+=1
    print(int(cnt))



resolve()
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    s = str(input())
    t = str(input())
    cnt=0
    for i in range(3):
        if s[i]==t[i]:
            cnt+=1
    print(cnt)



    
resolve()
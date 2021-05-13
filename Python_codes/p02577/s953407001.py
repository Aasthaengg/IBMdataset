import sys, os.path

if(os.path.exists('input.txt')):
    sys.stdin = open('input.txt',"r")
    sys.stdout = open('output.txt',"w")

sys.setrecursionlimit(10 ** 5)

def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))

def solve():
    sum=0
    lst = list(input())
    for _ in range(len(lst)):
        sum+=int(lst[_])
    if sum%9==0:
        print("Yes")
    else:
        print("No")
solve()
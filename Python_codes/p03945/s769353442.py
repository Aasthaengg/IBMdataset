import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    lst = [s[0]]

    for char in s[1:]:
        if lst[-1] != char:
            lst.append(char)

    ans = len(lst)-1
    print(ans)
main()

import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    
    n = I()
    ans = 0
    x, y, z = 0, 0, 0

    for _ in range(n):
        s = S()
        ans += s.count("AB")
        if s[0]=="B" or s[-1]=="A":
            if s[0]=="B" and s[-1]=="A":
                x += 1
            elif s[0]=="B":
                z += 1
            else:
                y += 1
    
    if x==0:
        ans += min(y,z)
    else:
        if y==0 or z==0:
            if y==0 and z==0:
                ans += x-1
            else:
                ans += x
        else:
            ans += x + 1 + min(y-1, z-1)

    print(ans)
                


main()

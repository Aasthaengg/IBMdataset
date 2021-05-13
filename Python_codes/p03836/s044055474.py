import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    sx, sy, tx, ty = LI()
    tx -= sx
    ty -= sy
    x = abs(tx)
    y = abs(ty)
    r,l,u,d = "r","l","u","d"
    ans = ""

    if tx != 0 and ty != 0:
        ans = r*x+u*y+l*x+d*(y+1)+r*(x+1)+u*(y+1)+l+u+l*(x+1)+d*(y+1)+r

        if tx<0:
            ans = ans.replace(r, "L")
            ans = ans.replace(l, "R")
        if ty<0:
            ans = ans.replace(u,"D")
            ans = ans.replace(d,"U")
            
        ans = ans.upper()
        
    else:
        x = max(x,y)
        ans = r*x+u+l*x+d*2+r*x+u+r+u*2+l*(x+2)+d*2+r

        if ty>0:
            ans = ans.replace(r,"U").replace(l,"D").replace(u,"L").replace(d,"R")
        elif tx<0:
            ans = ans.replace(r,"L").replace(l,"R")
        elif ty<0:
            ans = ans.replace(r,"D").replace(l,"U").replace(u,"R").replace(d,"L")
        ans = ans.upper()

    print(ans)
main()

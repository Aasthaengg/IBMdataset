import sys

def solve():
    W,H,x,y,r = map(int,input().split())
    print("Yes") if 0 <= x-r and W >= x+r and 0 <= y-r and H >= y+r else print("No")
    
solve()

from sys import stdin

def solve() :
    X,Y = [int(x) for x in stdin.readline().rstrip().split()]

    if(X % Y != 0):
        print(X)
    else :
        print(-1)

solve();
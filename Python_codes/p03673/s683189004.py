from sys import stdin
from collections import deque
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    d=deque([])
    for i in range(n):
        if i%2==0:
            d.append(a[i])
        else:
            d.appendleft(a[i])

    if n%2==1: d.reverse()
    print(*d)

if __name__=="__main__":
    main()
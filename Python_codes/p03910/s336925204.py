import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    ok = n
    ng = 0

    while ok-ng > 1:
        middle = (ok+ng)//2
        max_score = (middle)*(middle+1)//2
        if max_score >= n:
            ok = middle
        else:
            ng = middle
    
    ans_lst = []
    num = ok

    while n != 0:
        if n > num:
            ans_lst.append(num)
            n -= num
            num -= 1
        else:
            ans_lst.append(n)
            n -= n

    print(*ans_lst, sep="\n")

    # print(ok*(ok+1)//2, ok*(ok-1)//2,sum(ans_lst))

main()

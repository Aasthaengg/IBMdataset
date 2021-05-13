import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    s = s.split("><")
    ans_lst = []

    for part in s:
        lnum = part.count("<")
        rnum = part.count(">")      
        ans_lst.append(lnum*(lnum+1)//2 + rnum*(rnum+1)//2 + max(lnum,rnum)+1)


    if len(s) == 1:
        lnum = s[0].count("<") -1
        rnum = s[0].count(">") -1
        ans_lst[0] = lnum*(lnum+1)//2 + rnum*(rnum+1)//2 + max(lnum,rnum)+1
    else:
        lnum = s[0].count("<") -1
        rnum = s[0].count(">")
        ans_lst[0] = lnum*(lnum+1)//2 + rnum*(rnum+1)//2 + max(lnum,rnum)+1

        lnum = s[-1].count("<")
        rnum = s[-1].count(">") -1
        ans_lst[-1] = lnum*(lnum+1)//2 + rnum*(rnum+1)//2 + max(lnum,rnum)+1

    ans = sum(ans_lst)
    print(ans)

main()

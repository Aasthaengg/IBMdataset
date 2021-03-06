import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():


    s = S()
    t = S()
    
    dic1 = collections.defaultdict(str)
    dic2 = collections.defaultdict(str)
    
    for i in range(len(s)):
        if dic1[t[i]] == "":
            dic1[t[i]] = s[i]
        else:
            if dic1[t[i]] != s[i]:
                print("No")
                exit(0)

        if dic2[s[i]] == "":
            dic2[s[i]] = t[i]
        else:
            if dic2[s[i]] != t[i]:
                print("No")
                exit(0)
        
    print("Yes")

main()

import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    S = list(input())

    ans = []
    for s in S:
        o = ord(s) + N
        if ord('Z') < o:
            o = o - ord('Z') + 64
        
        ans.append(chr(o))
    
    print("".join(ans))




if __name__ == "__main__":
    main()
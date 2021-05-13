import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    S = list(input())
    T = list(input())

    t = len(T)
    ans = INF
    for i in range(len(S)):
        s = S[i:i+t]
        if len(s) != t: break

        diff = 0
        for j in range(t):
            diff += s[j] != T[j]
        
        ans = min(ans,diff)

    print(ans)



if __name__ == "__main__":
    main()
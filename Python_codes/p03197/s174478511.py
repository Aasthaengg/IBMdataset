import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    ans=1
    for i in range(N):
        a=I()
        if a%2==1:
            ans=0
            break
        
    S=["first","second"]
    print(S[ans])
                
    #奇数があれば先手の勝ち？
    #帰納法で証明できそう

main()

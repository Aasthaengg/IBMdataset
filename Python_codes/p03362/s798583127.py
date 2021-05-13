import math
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

def get_prime(n): 
    X = [i for i in range(2,n+1)] 
    prime = []
    mx = math.sqrt(n) + 1 

    while True:
        p = min(X) 
        if mx <= p:
            prime.extend(X) 
            break
        prime.append(p) 
        X = [i for i in X if i % p != 0]

    return prime




INF=10**20
def main():
    N = ii()
    P = set(get_prime(55555))

    ans = [2]
    p = 2
    while len(ans) < N:
        p += 5
        while p < 55555 and not p in P:
            p += 5
        
        ans.append(p)
    
    # print(sum(ans))
    print(*ans,sep=' ')
        






if __name__ == "__main__":
    main()
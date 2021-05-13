import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    import bisect
    
    mod=10**9+7
    N=I()
    L=LI()
    L.sort()
    ans=0
    for i in range(N):
        for j in range(i+1,N):
            a=L[i]
            b=L[j]
            ab=a+b
            num=bisect.bisect_left(L,ab)
            
            # print(i,j,num-j)
            ans+=num-j-1
            
                
    print(ans)
    

main()

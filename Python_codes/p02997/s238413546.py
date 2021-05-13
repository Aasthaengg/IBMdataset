import sys
input = sys.stdin.readline
INF = 10 ** 9
MOD = 10 ** 9 + 7

def main(): 
    n,k = map(int,input().split())
    
    if k > (n-1)*(n-2)//2:
        print(-1)
        exit()
    
    print(n*(n-1)//2 - k)
    for i in range(2,n+1):
        print(1,i)
    
    x = (n-1)*(n-2)//2 - k
    i = 2
    j = 3
    while x > 0:
        x -= 1
        print(i,j)
        j += 1
        if j == n + 1:
            i += 1
            j = i + 1
   
if __name__=='__main__':
    main()

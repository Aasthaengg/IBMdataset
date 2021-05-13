import sys
input = sys.stdin.readline
INF = 10 ** 9
MOD = 10 ** 9 + 7

def main(): 
    h,w,d = map(int,input().split())
    n = h * w

    idx = [0]*(1+n)
    for i in range(h):
        a = tuple(map(int,input().split()))
        for j in range(w):
            idx[a[j]] = (i + 1 , j + 1)
    idx[0] = idx[d]

    D = [0] * (n + 1)
    
    def dist(i,j):
        return abs(idx[i][0] - idx[j][0]) + abs(idx[i][1] - idx[j][1])
        
    for i in range(d):
        for j in range(i,n - d + 1,d):
            D[j + d] = D[j] + dist(j,j + d)
    
    q = int(input())
    for _ in range(q):
        l,r = map(int,input().split())
        print(D[r] - D[l])        

if __name__=='__main__':
    main()


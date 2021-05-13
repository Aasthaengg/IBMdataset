import sys
input=sys.stdin.readline

def main():
    n = int(input())
    
    A = [0]*n
    B = [0]*n
    C = [0]*n
    
    a,b,c = map(int,input().split())
    A[0] = a
    B[0] = b
    C[0] = c
    
    for i in range(1,n):
        a,b,c = map(int,input().split())
        A[i] = max(B[i-1]+a, C[i-1]+a)
        B[i] = max(A[i-1]+b, C[i-1]+b)
        C[i] = max(A[i-1]+c, B[i-1]+c)
    
    print(max(A[n-1], B[n-1], C[n-1]))
    
if __name__ == '__main__':
    main()
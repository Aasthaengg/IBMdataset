import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    A = list(map(int,input().split()))
    a,b = max(A), min(A)
    ap,bp = A.index(a),A.index(b)
    ans = []
    if a >= -b:
        for i in range(N):
            if A[i] < 0:
                A[i] += a
                ans.append([ap+1,i+1])
        for i in range(N-1):
            A[i+1] += A[i]
            ans.append([i+1,i+2])
    else:
        for i in range(N):
            if A[i] > 0:
                A[i] += b
                ans.append([bp+1,i+1])
        for i in range(N-1):
            A[-i-2] += A[-i-1]
            ans.append([N-i,N-i-1])
            
    L = len(ans)
    print(L)
    for i in range(L):
        print(*ans[i])
        
if __name__ == "__main__":
    main()
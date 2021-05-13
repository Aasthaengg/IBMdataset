def main():
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    A = list(map(int,input().split()))
    big = 0
    I = 0
    for i in range(len(A)):
        if abs(big) < abs(A[i]):
            big = A[i]
            I = i
    
    ansN = 0
    ans = []
    
    if big > 0:
        ansN = 2*N
        ans.append([I+1,I+1])
        ans.append([I+1, 1])
        for i in range(1,N):
            ans.append([i,i+1])
            ans.append([i,i+1])
    elif big < 0:
        ansN = 2*N
        ans.append([I+1, I+1])
        ans.append([I+1, N])
        for i in range(N-1):
            j = N - i
            ans.append([j, j-1])
            ans.append([j, j-1])
    print(ansN)
    for i in ans:
        print(*i)
        j,k = i
        A[k-1] += A[j-1]
    #print(*A)
        
    
    
main()
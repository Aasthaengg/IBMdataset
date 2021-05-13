def solve(): 

    N = int(input())
    A = list(map(int, input().split()))

    i = 0
    result = 0

    while i < N:
        while i+1 < N and A[i] == A[i+1]:
            i += 1
        if i+1 < N and A[i] < A[i+1]:
            while i+1 < N and A[i] <= A[i+1]:
                i += 1
        elif i+1 < N and A[i] > A[i+1]:
            while i+1 < N and A[i] >= A[i+1]:
                i += 1
        
        result += 1
        i += 1

    print(result)    

if __name__ == "__main__":
    solve()

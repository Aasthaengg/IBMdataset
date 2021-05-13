def main():
    Hit,N = map(int, input().split())
    A = [0]*N
    B = [0]*N
    H = [-1]*(10**5+10000)
    mi = 10**10
    for i in range(N):
        A[i] ,B[i] = map(int, input().split())
    for i in range(N):
        H [A[i]] = B[i] if H[A[i]] == -1 else min(H [A[i]],B[i])
        if A[i] >= Hit:
            mi = min(mi,B[i])
        for j in range(Hit+1):
            if H[j]!=-1:
                H[j+A[i]] = B[i] + H[j] if H[j+A[i]] == -1 else min(H[j+A[i]],B[i]+H[j])
                if j+A[i] >= Hit:
                    mi = min(mi,B[i] + H[j])
    print(mi)






if __name__ == '__main__':
    main()
def main(N,M):
    if N >= 3 and M >= 3:
        return (N-2)*(M-2)
    elif N <= 2 and M <= 2:
        return 0 if (N*M) % 2 == 0 else 1
    else:
        if min(N,M) == 1:
            return max(N,M)-2
        else:
            return 0
N,M = map(int,input().split())
print(main(N,M))
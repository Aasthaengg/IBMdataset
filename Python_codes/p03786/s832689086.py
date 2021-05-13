from itertools import accumulate
from bisect import bisect_left as bl
def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = N
    tmp = 0
    B = list(accumulate(A))
    for i,b in enumerate(B):
        k = bl(A,b*2)
        if k == N:continue
        if A[k-1] == A[i] and A[k] > 2*b:
            tmp = i+1
    ans -= tmp
    
    print(ans)
if __name__ == "__main__":
    main()
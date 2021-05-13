import bisect
import sys

def main(args):
    
    n = int(input())
    A = list(map(int,input().split()))
    
    A.sort()
    
    ans = [max(A), 0]
    ind = bisect.bisect_left(A ,ans[0]//2)
    if A[ind] == ans[0]//2:
        ans[1] = ans[0]//2
    else:
        r1 = min(A[ind],ans[0]-A[ind])
        r2 = min(A[ind-1],ans[0]-A[ind-1])
        if r1 > r2:
            ans[1] = A[ind]
        else:
            ans[1] = A[ind-1]
    
    print(*ans)
    
if __name__ == '__main__':
    main(sys.argv[1:])
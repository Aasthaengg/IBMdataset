n,k = map(int,input().split())
A = list(map(int,input().split()))

def is_ok(s):
    cnt = 0
    for i in range(n):
        cnt += (A[i]-1)//s
    return cnt<=k
def main():
    left = 0
    right = max(A)
    while (right-left)>1:
        mid = (right+left)//2
        if is_ok(mid):
            right = mid
        else:
            left = mid
    return right
print(main())

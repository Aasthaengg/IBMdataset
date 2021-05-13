import math

def solve(x):
    cnt = 0
    for i in li:
        k_i = math.ceil(i/x) - 1
        cnt += k_i
    if cnt > k:
        return False
    else:
        return True


n=0
k=0
li=[]

if __name__ == "__main__":
    n,k = map(int, input().split())
    li = list(map(int,input().split()))
    left = 1
    right = 10**9
    ans = 0
    while right >= left:
        mid = left + (right - left)//2
        flag = solve(mid)
        if flag:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)

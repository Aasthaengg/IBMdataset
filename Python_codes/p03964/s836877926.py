from math import ceil
def solve():
    N = int(input())
    T = []
    A = []
    for _ in range(N):
        t, a = map(int,input().split())
        T.append(t)
        A.append(a)
    
    now_t = T[0]
    now_a = A[0]

    for i in range(1,N):
        mul = f(now_t,now_a,T[i],A[i])
        now_t = T[i] * mul
        now_a = A[i] * mul
    
    print(now_t + now_a)

def f(now_t, now_a, t, a):
    left = 0
    right = 10 ** 18
    while right - left > 1:
        mid = (right + left) // 2
        if now_t > t * mid or now_a > a * mid:
            left = mid
        else:
            right = mid
    
    return right

if __name__ == '__main__':
    solve()
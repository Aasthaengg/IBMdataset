#2,3
#3,4

def main():
    N = int(input())
    A = [int(_n) for _n in input().split()]
    B = [int(_n) for _n in input().split()]
    max_h = [10**10]*N
    min_h = [1]*N
    prev = -1
    for i in range(N):
        a = A[i]
        if prev != a:
            max_h[i] = a
            min_h[i] = a
        else:
            max_h[i] = max_h[i-1]
            min_h[i] = 0
        prev = a
    prev = -1
    res = 1
    MOD = 10**9+7
    for i in reversed(range(N)):
        a = B[i]
        new_range = [0,0]
        if prev != a:
            new_range[0] = a
            new_range[1] = a
        else:
            new_range[0] = max_h[i+1]
            new_range[1] = 1
        if max_h[i] < new_range[1] or min_h[i] > new_range[0]:
            print(0)
            return
        max_h[i] = min(max_h[i], new_range[0])
        min_h[i] = max(min_h[i], new_range[1])
        # print(max_h[i],min_h[i])
        res = (max_h[i]-min_h[i]+1) * res % MOD
        prev = a
    print(res)



main()
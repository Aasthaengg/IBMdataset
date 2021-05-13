def main():
    from bisect import bisect_right
    N = int(input())
    A = sorted(list(map(int,input().split())))
    B = sorted(list(map(int,input().split())))
    C = sorted(list(map(int,input().split())))
    
    num_greater_than_b = []
    for b in B:
        num_greater_than_b.append(N-bisect_right(C,b))

    csum = [0]*(N+1)
    for i in range(N-1,-1,-1):
        csum[i] = csum[i+1]+num_greater_than_b[i]
        
    ans = 0
    for i,a in enumerate(A):
        ans += csum[bisect_right(B,a)]
    print(ans)
main()


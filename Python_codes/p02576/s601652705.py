def main(N,X,T):
    count=0
    ans = 0
    while count < N:
        count += X
        ans += T
    return ans

N,X,T=map(int, input().split())
print(main(N,X,T))
N = int(input())

def gauss_count(n):
    return n*(n+1)//2

print(sum(x * gauss_count(N//x) for x in range(1, N+1)))

def combination(n):
    return n * (n-1) // 2

n,m = map(int,input().split())
print(combination(n) + combination(m))
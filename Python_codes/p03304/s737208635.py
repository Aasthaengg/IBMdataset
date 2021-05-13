
def f(n, m, d):
    if d == 0:
        return (m-1)/n
   
    numerator = m-1
    denom = n*n

    numerator *= (2*(n-d))
   
    return numerator / denom
   
n, m, d = [int(i) for i in input().split()]
print(f(n, m, d))
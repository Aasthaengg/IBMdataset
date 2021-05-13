a, b = map(int, input().split())
def calc(m,B, i):
    if (i*(m-1) >= B-1):
        return i
    return calc(m,B, i+1)
print(calc(a,b,i=0))
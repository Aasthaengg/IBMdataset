def gcd(x, y):
    if x == 0: return y
    return gcd(y%x, x)
lcm = lambda x, y: x*y//gcd(x, y)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = [e//2 for e in arr]

cm = arr[0]
for e in arr[1:]:
    cm = lcm(cm, e)

if any([cm//e % 2 == 0 for e in arr]):
    print(0)
    exit()
print((m//cm+1)//2)

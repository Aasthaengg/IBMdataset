n, a, b = map(int, input().split())
if n==1:
    if a==b:
        val = 1
    else:
        val = 0
else:
    if a > b:
        val = 0
    else:
        val = ((n-2)*b-(n-2)*a)+1
print(val)
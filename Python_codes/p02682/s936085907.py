a,b,c,k = map(int,input().split())
if k <= a:
    print(k)
    quit()
if k <= a + b:
    print(a)
    quit()
print(a - (k - b - a))
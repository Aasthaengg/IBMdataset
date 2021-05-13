import bisect
x, n = map(int, input().split())
pN = list(map(int, input().split()))

pN.sort()

diff = 0

if n == 0:
    print(x)
else:
    while(1):
        if x-diff not in pN:
            print(x-diff)
            exit()
        elif x+diff not in pN:
            print(x+diff)
            exit()
        diff+=1
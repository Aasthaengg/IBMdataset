import fractions
n,k = map(int,input().split())
ai = [int(i) for i in input().split()]

if n == 1:
    if k == ai[0]:
        print('POSSIBLE')
        exit()
    else:
        print('IMPOSSIBLE')
        exit()

g = fractions.gcd(ai[0],ai[1])

for i in range(1,n-1):
    #print(i)
    g = fractions.gcd(g,ai[i+1])

if k % g == 0 and max(ai) >= k:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
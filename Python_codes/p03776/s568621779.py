from math import factorial

def nCr(n, r) :
    return factorial(n)//(factorial(r)*factorial(n-r))


n,a,b = map(int,input().split())
V = sorted(list(map(int,input().split())), reverse=True)

L1, L2 = V[:a], V[a:]

ans1 = sum(L1)/a

minv = min(L1)
x = L1.count(minv)
y = L2.count(minv)

ans2 = 0

if x == a :
    for i in range(x, x+min(y, b-a)+1) :
        ans2 += nCr(x+y, i)
else :
    ans2 = nCr(x+y, x)

print(ans1)
print(ans2)

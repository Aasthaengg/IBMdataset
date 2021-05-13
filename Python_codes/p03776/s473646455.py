
n, a, b = map(int,input().split())
V = list(map(int,input().split()))

V.sort(reverse=True)

print(sum(V[:a]) / a)

D = {}
Da = {}

for i in range(n):
    try:
        D[V[i]] += 1
    except:
        D[V[i]] = 1

for i in range(a):
    try:
        Da[V[i]] += 1
    except:
        Da[V[i]] = 1



def C(x, y):
    ans = 1
    for i in range(x, x-y, -1):
        ans *= i
    for i in range(1, y+1):
        ans //= i
    return ans

#print(C(5,3))

if len(set(V[:a])) > 1:
    ans = 1
    for i in set(V[:a]):
        ans *= C(D[i], Da[i])

else:
    ans = 0
    for i in range(a, b+1):
        #print(D[V[0]], i)
        ans += C(D[V[0]], i)

print(ans)
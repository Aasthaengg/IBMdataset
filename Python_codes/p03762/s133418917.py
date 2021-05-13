a,b = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
s = 0 
k = 0
for i,t in enumerate(reversed(x)):
    s+= (a-i-1)*t
    s-= i*t
for i,t in enumerate(reversed(y)):
    k+= (b-i-1)*t
    k-= i*t
print((s*k)%(10**9+7))

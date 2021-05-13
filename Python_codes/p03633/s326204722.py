def lcm(a, b): #lcm(int, int)
    if a<b:
        a,b = b,a
    x = a*b
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a % b
    return x//b
n = int(input())
t = [0]*n
for i in range(n):
    t[i] = int(input())
ans = t[0]
for i in range(1,n):
    ans = lcm(ans,t[i])
print(ans)
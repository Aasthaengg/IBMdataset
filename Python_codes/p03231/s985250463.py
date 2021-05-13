import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

n,m = map(int,input().split())
S = input()
T = input()

l = lcm(n,m)
i = 0
j = 0
ans = l
while i < n or j < m:
    temp_n = i*l//n+1
    temp_m = j*l//m+1
    if temp_n == temp_m:
        if S[i] != T[j]:
            ans = -1
            break
        i += 1
        j += 1
    elif temp_m > temp_n:
        i += 1
    else:
        j += 1

print(ans)
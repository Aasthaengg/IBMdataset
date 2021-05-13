def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
A, B, C, D = list(map(int,input().rstrip().split()))
lcm = int(C/gcd(C,D)*D)
ans = B-A+1
ans -= B//C-(A-1)//C
ans -= B//D-(A-1)//D
ans += B//lcm-(A-1)//lcm
print(ans)
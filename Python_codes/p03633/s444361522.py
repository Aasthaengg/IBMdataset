import sys
sys.setrecursionlimit(10**6)
n = int(input().rstrip())
seconds = [int(input().rstrip()) for _ in range(n)]
#seconds = list(set(seconds))

def gcd(a,b):
    if int(b) == 0:
        return int(a)
    return gcd((b),(a%b))
def lcm(a,b):
    g = gcd(a,b)
    if a<b:
        return int(a/g)*b
    else:
        return int(b/g)*a

ans = 1
for num in seconds:
    ans = int(lcm(ans,num))
print(ans)
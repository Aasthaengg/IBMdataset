n,k =map(int,input().split())
if n//k != 0:
        n -= (n//k)*k
else:
        pass
def p(n):
        if n > abs(n-k):
                return True
        else:
                return False
while p(n):
        n = abs(n-k)

print(n)

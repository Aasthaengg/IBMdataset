import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()

# N = q*m+m = (q+1)*m になることに注目

divisor = []  # Nの約数
for i in range(1,int(N**.5)+1):
    if N % i == 0:
        divisor.append(i)
        if i != N//i:
            divisor.append(N//i)

ans = 0
for d in divisor:
    m = d-1
    if N//d < m:
        ans += m

print(ans)

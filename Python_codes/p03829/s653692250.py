n,a,b = map(int,input().split())
xi = [int(i) for i in input().split()]

ans = 0

for i in range(1,n):
    tmp_a = (xi[i] - xi[i-1])*a
    if tmp_a >= b:
        ans += b
    else:
        ans += tmp_a
        
print(ans)
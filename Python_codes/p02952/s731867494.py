N = input()
l = len(N)
N_i = int(N)
ans = 0
 
p = int(l/2)
for i in range(p):
    q = i*2
    ans += 9 * (10**q)
 
if l%2 != 0:
    bottom = 10**(l-1)
    ans += N_i - bottom + 1
 
print(ans)
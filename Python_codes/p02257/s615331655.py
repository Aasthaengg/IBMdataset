# coding: utf-8

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1
    
ans = 0
n = int(input())
for i in range(n):
    if is_prime(int(input())):
        ans += 1
    
print(ans)
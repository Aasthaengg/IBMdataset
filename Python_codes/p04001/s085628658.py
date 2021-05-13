s = list(input())
n = len(s)-1
ans = 0
l = []
for i in range(2**n):
    ss = s.copy()
    for j in range(n):
        bit = (i >> j) & 1
        if bit == 1:
            ss.insert(n - j, '+')

    ans += eval(''.join(ss))      

 
print(ans)
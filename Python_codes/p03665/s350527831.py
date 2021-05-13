a, b = map(int, input().split())
c = [int(i)&1 for i in input().split()]
odd = sum(c)
val = 0
if odd:
    val = 2**(a-1)
else:
    val = 2**a*(1-b)
 
print(val)
n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
 
min_limit = min(a, b, c, d, e)
if n % min_limit == 0:
    cnt = n // min_limit
else:
    cnt = n // min_limit + 1
print(5 + cnt - 1)
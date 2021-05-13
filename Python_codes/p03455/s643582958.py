a,b = input().split()
_a = True if int(a)%2==0 else False
_b = True if int(b)%2==0 else False
res = 'Even' if _a or _b else 'Odd'
print(res)
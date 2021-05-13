n = int(input())
a = n // 111
b = n % 111
if b > 0:
    ans = (a + 1) * 111
else:
    ans = a * 111   
print(ans)
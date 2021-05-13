n = int(input())
seq = [int(x) for x in input().split()]
div4 = sum((1 for i in seq if i % 4 == 0))
div2 = sum((1 for i in seq if i % 2 == 0 and i % 4 != 0))
odd = n - div4 - div2
ans = "Yes"
if n == 2:
    if div4 == 0:
        if div2 != 2:
            ans = "No"
elif n == 3:
    if div4 == 0:
        if div2 != 3:
            ans = "No"
elif odd - div4 == 1 and odd+div4 == n:
    pass 
elif div4 < odd:
    ans = "No"
elif (div4 - odd) + div2 < 1:
    ans = "No"
print(ans)
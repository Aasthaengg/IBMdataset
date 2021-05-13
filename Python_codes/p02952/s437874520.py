n = int(input())

ans = 0
if len(str(n)) == 1:
    ans = n
elif len(str(n)) == 2:
    ans = 9
elif len(str(n)) == 3:
    ans = 9 + (n-99)
elif len(str(n)) == 4:
    ans = 909
elif len(str(n)) == 5:
    ans = 909 + (n-9999)
else:
    ans = 90909
print(ans)
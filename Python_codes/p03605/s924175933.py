n = int(input())
ans = "No"
while n:
    q, r = divmod(n, 10)
    if r == 9:
        ans = "Yes"
        break
    n = q
print(ans)
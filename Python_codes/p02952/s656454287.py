def ketaodd(n):
    if len(str(n)) % 2 != 0:
        return True
    else:
        return False
m = int(input())
ans = 0
for i in range(1,m+1):
    ans += ketaodd(i)
print(ans)
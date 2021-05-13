n = int(input())
 
ans = []
while n != 0:
    if n % 2 != 0:
        n -= 1
        ans.append("1")
    else:
        ans.append("0")
    n //= -2
 
if len(ans) == 0:
    ans.append("0")
 
print("".join(reversed(ans)))
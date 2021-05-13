n = int(input())
n -= 1
for i in range(1, 15):
    if n >= 26**i :
        n -= 26**i
        continue 
    ans = ""
    for j in range(i):
        d = n % 26
        ans += chr(ord("a")+d)
        n //= 26
    ans = ans[::-1]
    break
print(ans)




s = str(input())

n = len(s)-1
ans = 0
for i in range(2**n):
    op = [""]*n
    for j in range(n):
        if (i>>j)&1:
            op [n - 1 - j] = "+"
    formula = ""
    for p1 ,p2 in zip(s, op + [""]):
        formula += (p1 + p2)
    ans += eval(formula)

print(ans)
  
        

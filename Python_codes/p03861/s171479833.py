a, b, x = map(int, input().split())
an = a%x
if an != 0:
    an = x - an
if a + an > b:
    ans = 0
else:
    ans = (b-a-an)//x + 1
print(ans)
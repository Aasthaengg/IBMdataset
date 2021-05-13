x = int(input())
double, rest = divmod(x, 11)
if rest == 0:
    add = 0
elif 1<= rest <= 6:
    add = 1
else:
    add = 2
ans = double * 2 + add
print(ans)
X = int(input())
amari = X % 100
a = (X-amari)//100
if a*5 >= amari:
    ans = 1
else:
    ans = 0
print(ans)

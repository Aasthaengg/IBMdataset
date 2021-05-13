n, y = map(int, input().split())
 
f = True
 
for i in range(y // 10000 + 1):
    for j in range((y - 10000 * i) // 5000 + 1):
        if 10000 * i + 5000 * j + 1000 * (n - i - j) == y:
            ans = "{} {} {}".format(i, j, n - i - j)
            print(ans)
            f = False
            exit()
        else:
            pass
 
if f:
   print("-1 -1 -1")
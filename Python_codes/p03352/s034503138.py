X = int(input())

ans = 1
for b in range(1, X + 1):
    for p in range(2, 11):
        a = b ** p
        if a <= X and ans < a:
           ans = a

print(ans)
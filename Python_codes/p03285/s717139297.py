n = int(input())
ans = "No"
for cake_n in range(30):
    for donut_n in range(15):
        if n == cake_n * 4 + donut_n * 7:
            ans = "Yes"
print(ans)

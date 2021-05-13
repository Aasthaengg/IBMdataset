X = int(input())

ans = 0
for i in range(1, 101):
    for j in range(2, 101):
        if i ** j <= X:
            if i ** j > ans:
                ans = i ** j
print(ans)

N = int(input())

C = 4
D = 7
value = 0
ans = "No"

for i in range(100):
    for j in range(100):
        value = C * i + D * j
        if value == N:
            ans = "Yes"
            break

print(ans)

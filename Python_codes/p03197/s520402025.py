n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
winner = "second"
for i in a:
    if i%2 == 1:
        winner = "first"
print(winner)
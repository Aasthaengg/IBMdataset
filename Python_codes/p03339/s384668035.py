n = int(input())
s = str(input())

east = s.count("E")
west = 0
ans = 300000
for i in range(n):
    if s[i] == "E":
        east -= 1
    ans = min(ans, east + west)
    if s[i] == "W":
        west += 1

print(ans)

n, k = map(int, input().split())
s = input()

target = "R" if s[0] == "L" else "L"
s = "N" + s + "N"
happy_count = 0
position = []
for i in range(1, len(s)-1):
    if s[i] == "R" and s[i+1] == "R":
        happy_count += 1
    elif s[i] == "L" and s[i-1] == "L":
        happy_count += 1
    if s[i] == target and s[i+1] != target:
        position.append(i)

for i in range(len(position)):
    if k == 0:
        break
    if position[i] == n:
        happy_count += 1
    else:
        happy_count += 2
    k -= 1

print(happy_count)

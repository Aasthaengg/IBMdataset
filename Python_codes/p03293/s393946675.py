#61
s = input()
t = input()
l = len(s)

mozi = s*2
ans = "No"

for i in range(l):
    if mozi[i:i+l] == t:
        ans = "Yes"
        break

print(ans)

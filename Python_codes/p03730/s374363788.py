a, b, c = [int(x) for x in input().split()]
i = temp = 0
temp_set = set()
ans = "NO"
while temp not in temp_set:
    temp_set.add(temp)
    if temp == c:
        ans = "YES"
        break
    i += 1
    temp = (a * i) % b
print(ans)
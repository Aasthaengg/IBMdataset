s = input()
l = [char for char in s]
ans = 0
c = 0
for val in range(len(l)):
    if l[val] == "W":
        ans += (val - c)
        c+=1
print(ans)
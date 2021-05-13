n = int(input())
s = input()
change = s.count("E")
ans = change
i_o = "dum"
for i in s:
    #print(change)
    if i == "E":
        change -= 1
    if i_o == "W":
        change += 1
    ans = min(change,ans)
    i_o = i
print(ans)
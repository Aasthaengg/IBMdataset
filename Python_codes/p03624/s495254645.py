s_set = set(input())
ord_a = ord("a")
ans = "None"
for i in range(26):
    c = chr(ord_a + i)
    if c not in s_set:
        ans = c
        break
print(ans)
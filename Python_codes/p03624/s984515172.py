S = input()

ans = "None"

for i in range(ord("a"), ord("z") + 1):
    if not chr(i) in S:
        ans = chr(i)
        break
print(ans)
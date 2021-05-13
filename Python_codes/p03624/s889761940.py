s = list(input())

s.sort()

ans = "None"
for i in range(97,123):
    if s.count(chr(i)) == 0:
        ans = chr(i)
        break

print(ans)
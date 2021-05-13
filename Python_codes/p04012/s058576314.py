s=str(input())
ans="Yes"
for i in set(s):
    if s.count(i) % 2 != 0:
        ans="No"
        break

print(ans)
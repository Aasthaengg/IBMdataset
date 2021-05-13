s = str(input())
ans = 'None'
for j in range(97, 123):
    if chr(j) in s:
        continue
    else:
        ans = chr(j)
        break
print(ans)
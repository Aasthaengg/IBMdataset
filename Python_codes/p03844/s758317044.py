i = list(input().split())
if i[1] == '+':
    ans = int(i[0]) + int(i[2])
else:
    ans = int(i[0]) - int(i[2])
print(ans)
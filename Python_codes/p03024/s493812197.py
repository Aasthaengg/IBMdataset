s = input()

cnt = 0
for c in s:
    if c == 'x':
        cnt += 1
if cnt >= 8:
    print("NO")
else:
    print("YES")

# print(*data, sep='\n')

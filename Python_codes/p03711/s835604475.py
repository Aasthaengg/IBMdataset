x, y = map(int, input().split())

dic = {'A': [1, 3, 5, 7, 8, 10, 12], 'B': [4, 6, 9, 11], 'C': [2]}

gx = 0
gy = 0
for key, value in dic.items():
    if x in value:
        gx = key
    if y in value:
        gy = key
ans = 'Yes' if gx == gy else 'No'
print(ans)

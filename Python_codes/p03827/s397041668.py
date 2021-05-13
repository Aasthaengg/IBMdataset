n = int(input())
s = list(input())
count = 0
ans = [0]
for i in s:
    if i == 'I':
        count += 1
    elif i == 'D':
        count -= 1
    ans.append(count)
print(max(ans))
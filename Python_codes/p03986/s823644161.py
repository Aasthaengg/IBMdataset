X = input()
s_count = 0
ans = 0
for i in X:
    if i == 'S':
        s_count += 1
    elif s_count > 0:
        s_count -= 1
        ans += 2
print(len(X)-ans)
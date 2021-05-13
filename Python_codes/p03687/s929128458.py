s = input()
num = len(s)
ans = num/2
if not ans.is_integer():
    ans = int(ans)+1

for i in range(num):
    a, b, count = s[i], [], 0
    for j in range(num):
        if s[j] != a:
            count += 1
        else:
            b.append(count)
            count = 0
        b.append(count)
    ans = min(ans, max(b))
print(int(ans))

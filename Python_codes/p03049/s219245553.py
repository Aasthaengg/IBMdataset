n = int(input())
a, b, c, ans = 0, 0, 0, 0
for i in range(n):
    word = input()
    ans += word.count('AB')
    if word[-1] == 'A' and word[0] == 'B':
        c += 1
    elif word[-1] == 'A':
        a += 1
    elif word[0] == 'B':
        b += 1

if c == 0:
    ans += min(a, b)
elif a+b > 0:
    ans += c+min(a, b)
elif a+b == 0:
    ans += c-1
print(ans)

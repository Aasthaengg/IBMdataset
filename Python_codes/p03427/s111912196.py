n = input()
l = len(n)
if l == 1:
    print(n)
    quit()
ans = 9 * (l - 1)
if n[1:] == '9' * (l - 1):
    ans += int(n[0])
else:
    ans += int(n[0]) - 1
print(ans)
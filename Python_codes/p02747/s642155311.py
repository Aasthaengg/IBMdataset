from sys import stdin
input = lambda: stdin.readline().rstrip()
s = input()
if len(s) % 2 == 1:
    print("No")
    exit()
ans = "Yes"
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] != "h":
            ans = "No"
            break
    else:
        if s[i] != 'i':
            ans = "No"
            break
print(ans)

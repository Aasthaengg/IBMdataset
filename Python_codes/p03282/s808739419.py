s = input()
k = int(input())

for i, a in enumerate(s):
    if a != "1":
        ans = 1 if k<=i else int(a)
        break
else:
    ans = 1
print(ans)

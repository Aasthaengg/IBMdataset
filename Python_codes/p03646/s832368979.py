k = int(input())
s = [i for i in range(51)]
s.reverse()
a = k % 50
b = k // 50
ans = []
for i in range(51):
    if not i == a:
        ans.append(s[i] + b)
print(50)
print(" ".join(map(str, ans)))
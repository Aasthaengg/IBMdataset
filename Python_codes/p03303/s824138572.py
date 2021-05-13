s = input()
w = int(input())
l = [s[i: i+w] for i in range(0, len(s), w)]
ans = ""
for i in range(len(l)):
    ans += l[i][0]
print(ans)

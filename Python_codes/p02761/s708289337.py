n, m = map(int, input().split())
num = ["A"] * n
for i in range(m):
    s, c = map(int, input().split())
    if n>1 and s == 1 and c == 0:
        print(-1)
        exit()
    elif num[s - 1] != "A" and num[s - 1] != c:
        print(-1)
        exit()
    num[s - 1] = c

for j in range(n):
    if num[j] == "A":
        num[j] = 0
    if n>1 and num[0] == 0:
        num[0] = 1
print(int("".join(map(str, num))))

n = int(input())
st = [input().split() for i in range(n)]
x = input()
flag = False
ans = 0
for i in st:
    if flag:
        ans += int(i[1])
    if i[0] == x:
        flag = True
print(ans)
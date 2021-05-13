n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(input().split())
haba = a[0]
for i in a:
    if int(haba[0]) <= int(i[0]) <= int(haba[1]):
        haba[0] = i[0]
    elif int(haba[1]) < int(i[0]):
        print(0)
        exit()
    if int(haba[0]) <= int(i[1]) <= int(haba[1]):
        haba[1] = i[1]
    elif int(i[1]) < int(haba[0]):
        print(0)
        exit()
if n < int(haba[0]):
    ans = 0
elif int(haba[0]) <= n <= int(haba[1]):
    ans = n - int(haba[0]) + 1
else:
    ans = int(haba[1]) - int(haba[0]) + 1
print(ans)
T = [int(input()) for _ in range(5)]

lst1 = []
lst2 = []
for i in range(5):
    if T[i]%10 == 0:
        lst1.append([0,T[i]])
    else:
        lst2.append([T[i]%10,T[i]])

lst2 = sorted(lst2, reverse=True)
lst = lst1 + lst2

ans = 0
for i in range(5):
    ans += lst[i][1]
    if lst[i][0] == 0:
        pass
    else:
        ans += 10 - lst[i][0]

if lst[i][0] == 0:
    pass
else:
    ans -= 10 - lst[i][0]

print(ans)

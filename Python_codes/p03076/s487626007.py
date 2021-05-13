menu = [int(input()) for i in range(5)]
def kuriage(n):
    if n %10 == 0:
        return 0
    else:
        return 10-(n %10)
ans = 0
mini = 10
k = 5
for i in range(5):
    if menu[i] %10 < mini and menu[i]%10 !=0:
        mini = menu[i] %10
        k = i
for i in range(5):
    if i == k:
        menu[i], menu[-1] = menu[-1], menu[i]

for i in range(5):
    if i != 4:
        ans += menu[i] + kuriage(menu[i])
    else:
        ans += menu[-1]
        print(ans)

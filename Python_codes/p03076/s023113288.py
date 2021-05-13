def chk(n):
    for i in range(14):
        if i*10 >= n:
            return i*10
    

menu = []
time = []
for i in range(5):
    menu.append(int(input()))
    time.append(menu[i]%10)
#print(menu,time)
min_i = [10,10]
for i in range(5):
    if time[i]!=0:
        if time[i]<min_i[0]:
            min_i[0] = time[i]
            min_i[1] = i
#print(min_i)
ans = 0
for i in range(5):
    if i == min_i[1]:
        ans += menu[i]
    else:
        ans += chk(menu[i])
print(ans)
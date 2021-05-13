time = 0
dif = [0] * 5
for i in range(5):
    y = int(input())
    x = (y + 9) // 10 * 10
    dif[i] = x-y
    time += x 
dif.sort(reverse = True)
time -= dif[0]
print(time)
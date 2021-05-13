time_list = [int(input()) for _ in range(5)]

new_list = []
for i in range(5):
    time = time_list[i]
    amari = 10 - int(str(time_list[i])[-1])
    if amari == 10:
        amari = 0
    new_list.append((time, amari))

new_list = sorted(new_list, key=lambda x: x[1])

total = 0
for i in range(4):
    total += new_list[i][0]
    total += new_list[i][1]

total += new_list[4][0]
print(total)

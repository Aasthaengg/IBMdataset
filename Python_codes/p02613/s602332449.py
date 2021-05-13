n = int(input())

arr = []
for it in range(n):
    arr.append(str(input()))

count_arr = [0] * 4

for i in arr:
    if i == 'AC':
        count_arr[0] += 1
    elif i == 'WA':
        count_arr[1] += 1
    elif i == 'TLE':
        count_arr[2] += 1
    elif i == 'RE':
        count_arr[3] += 1

# output
print('AC x', count_arr[0])
print('WA x', count_arr[1])
print('TLE x', count_arr[2])
print('RE x', count_arr[3])
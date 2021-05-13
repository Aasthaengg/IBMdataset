N = int(input())

max_min = 0
cumsum = 0
while cumsum <= 10 ** 7:
    max_min += 1
    cumsum += max_min
    if N <= cumsum:
        break

ans = [i + 1 for i in range(max_min)]
rm_value = cumsum - N
if rm_value != 0:
    ans.remove(rm_value)

for i in ans:
    print(i)

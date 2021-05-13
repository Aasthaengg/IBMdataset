ary = [0] * 1000000
for i in range(1, 1000 + 1):
    for j in range(2, 1000 + 1):
        val = i ** j
        # print(val)
        if val > 1000:
            break
        ary[val] += 1
x = int(input())
for i in range(x + 1):
    index = x - i
    if ary[index] > 0:
        break
print(index)
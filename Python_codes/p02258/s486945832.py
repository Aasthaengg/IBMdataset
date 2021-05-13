num = raw_input()
num_list = []
for i in range(int(num)):
        a = raw_input()
        num_list.append(int(a))

maxv = -10000000000000
minv = num_list[0]

for i in range(1, len(num_list)):
        maxv = max(maxv, num_list[i] - minv)
        minv = min(minv, num_list[i])

print maxv
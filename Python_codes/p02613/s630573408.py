n = int(input())
s = [input() for i in range(n)]

l = [0] * 4
sl = ['AC', 'WA', 'TLE', 'RE']
for i in s:
    if i == sl[0]:
        l[0] += 1
    elif i == sl[1]:
        l[1] += 1
    elif i == sl[2]:
        l[2] += 1
    else:
        l[3] += 1

for i in range(len(l)):
    print(sl[i] + ' x ' + str(l[i]))

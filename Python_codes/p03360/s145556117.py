s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])

v = input()
k = int(v)

max_index = 0

array = []
array.append(a)
array.append(b)
array.append(c)


for i in range(k):
    array.sort()
    x = array.pop()
    x *= 2
    array.append(x)


answer = 0
for i in range(len(array)):
    answer += array[i]

print(answer)


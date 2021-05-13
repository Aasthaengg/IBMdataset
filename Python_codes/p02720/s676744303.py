from collections import deque

k = int(input())

count = 1
d= deque([1,2,3,4,5,6,7,8,9])
#ls = []
while count <= k:
    v = d.popleft()
    count += 1
    last = str(v)[-1]
    if last == '0':
        d.append(int(str(v) + '0'))
        d.append(int(str(v)+'1'))
    elif last == '9':
        d.append(int(str(v) + '8'))
        d.append(int(str(v) + '9'))
    else:
        d.append(int(str(v) + str(int(last) - 1)))
        d.append(int(str(v) + str(int(last) )))
        d.append(int(str(v) + str(int(last) + 1)))
    #ls.append(v)

#print(ls)
print(v)
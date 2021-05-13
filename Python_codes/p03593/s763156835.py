from heapq import *
h, w = map(int, input().split())

char = [0]*26
for i in range(h):
    a = input()
    for j in range(w):
        char[ord(a[j])-97] -= 1

heapify(char)

q = []
if h % 2 == 1 and w % 2 == 1:
    for i in range((h//2)*(w//2)):
        q.append(4)
    for i in range((h+w-2)//2):
        q.append(2)
    q.append(1)

elif h % 2 == 1:
    for i in range((h//2)*(w//2)):
        q.append(4)
    for i in range(w//2):
        q.append(2)

elif w % 2 == 1:
    for i in range((h//2)*(w//2)):
        q.append(4)
    for i in range(h//2):
        q.append(2)

else:
    for i in range((h//2)*(w//2)):
        q.append(4)

flag = 1
for i in q:
    a = heappop(char)
    if -a >= i:
        a += i
        heappush(char, a)
    else:
        flag = 0
        break

if flag == 1:
    print("Yes")
else:
    print("No")

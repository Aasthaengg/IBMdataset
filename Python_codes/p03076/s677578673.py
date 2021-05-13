#ABC123-B
import numpy as np
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

tmp = [a,b,c,d,e]
time = []
for i in range(5):
    if tmp[i] % 10 != 0:
        s = ((tmp[i]) // 10 + 1)*10 - tmp[i]
    else:
        s = 0
    time.append(s)
    
idx = np.argmax(np.array(time))
last = tmp.pop(idx)
#print('tmp:',tmp)
#print('idx',idx)
result = 0
for j in range(4):
    if tmp[j] % 10 != 0:
        result += (tmp[j] // 10 + 1)* 10
    else:
        result += tmp[j]
        
result += last

print(result)


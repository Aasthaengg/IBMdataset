import numpy as np
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
s = [[a%10,a//10*10+10,a],[b%10,b//10*10+10,b],[c%10,c//10*10+10,c],[d%10,d//10*10+10,d],[e%10,e//10*10+10,e]]
s.sort()
for i in range(5):
    if s[0][0] == 0:
        s[0][1]-=10
        s.append(s.pop(0))
    else:
        break
s = np.array(s)
ans = s[0][2] + sum(s[1:,1])
print(ans)
d = input()

s = 0

for i in range(len(d)):
    s += int(d[i])
    
if (s%9) == 0:
    print("Yes")
else:
    print("No")
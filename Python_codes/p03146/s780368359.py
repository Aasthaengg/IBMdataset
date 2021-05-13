s = int(input())
num = [0]*1000006
num[s] = 1
a = []
a.append(s)
for i in range(1, 1000001):
    if a[-1] % 2 == 0:
        tmp = a[-1] // 2
    else:
        tmp = 3 * a[-1] + 1
    a.append(tmp)
    
    if num[tmp] == 1:
        print(i + 1)
        exit()
    
    num[tmp] = 1

n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
d.sort()
t.sort()
flag = True
num = 0
for i in range(m):
    while d[num] != t[i]:
        if d[num] > t[i]:
            flag = False
            break
        else:
            num += 1
    else:
        num += 1
    if flag == False:
        break
if flag == True:
    print("YES")
else:
    print("NO")

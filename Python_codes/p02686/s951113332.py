import sys
input = sys.stdin.readline

N = int(input())
array1 = []
array2 = []
for i in range(N):
    s = input()
    x1 = 0
    x2 = 0
    x3 = 0
    flag = True
    for j in range(len(s)):
        if s[j] == "(":
            if flag:
                x3 = 1
            else:
                x3 += 1
            flag = False
            x1 += 1
        elif s[j] == ")":
            x1 -= 1
            if flag:
                x2 += 1
            else:
                x3 -= 1
    if x3 < 0:
        x2 = x2 - x3
    if x1 >= 0:
        array1.append((-x2,x1))
    else:
        array2.append((x2+x1,-x2,x1))
array1.sort(reverse = True)
array2.sort(reverse = True)
sum = 0
ans = True
for i in range(len(array1)):
    if sum + array1[i][0] >= 0:
        sum += array1[i][1]
    else:
        ans = False
        break
for i in range(len(array2)):
    if sum + array2[i][1] >= 0:
        sum += array2[i][2]
    else:
        ans = False
        break
if sum != 0:
    ans = False
if ans:
    print("Yes")
else:
    print("No")

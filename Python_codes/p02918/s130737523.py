from sys import exit
n, k = map(int, input().split())
s = list(input())
if n == 1:
    print(0)
    exit()

L_record = []
R_record = []

if s[0] == "L":
    flg = "R"
else:
    flg = "L"

for i, char in enumerate(s):
    if char == "L" and flg == "R":
        L_record.append([i, 1])
        flg = "L"
    elif char == "L" and flg == "L":
        L_record[-1][1] += 1
    elif char == "R" and flg == "L":
        R_record.append([i, 1])
        flg = "R"
    elif char == "R" and flg == "R":
        R_record[-1][1] += 1

L_record.sort(key=lambda x: x[0])
R_record.sort(key=lambda x: x[0])
#print(L_record, R_record)

if L_record != []:
    if L_record[-1][0] + L_record[-1][1] == n:
        record = L_record.pop()
        L_record = [record] + L_record
if R_record != []:
    if R_record[-1][0] + R_record[-1][1] == n:
        record = R_record.pop()
        R_record = [record] + R_record


point = 0
for i, char in enumerate(s):
    #print(i, char)
    if char == "L" and i-1 >= 0:
        if s[i-1] == "L":
            point += 1
            #print(point)
    if char == "R" and i+1 < n:
        if s[i+1] == "R":
            point += 1
            #print(point)
#print(point)

#L -> R
point_l = point
for i in range(k):
    if L_record != []:
        idx, num = L_record.pop()
        if idx == 0:
            point_l += 1
        elif idx + num == n:
            point_l += 1
        else:
            point_l += 2

point_r = point
for i in range(k):
    if R_record != []:
        idx, num = R_record.pop()
        if idx == 0:
            point_r += 1
        elif idx + num == n:
            point_r += 1
        else:
            point_r += 2
print(min(max(point_r, point_l), n-1))
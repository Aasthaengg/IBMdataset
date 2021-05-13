from sys import stdin
n = int(input())
s = [stdin.readline()[:-1] for i in range(n-1)]
s.append(input())
ans = [0,0,0,0]
temp = ["AC","WA","TLE","RE"]
for i in s:
    if i=="AC":
        ans[0] += 1
    elif i=="WA":
        ans[1] += 1
    elif i=="TLE":
        ans[2] += 1
    else:
        ans[3] += 1
for i in range(4):
    print("{result} x {num}".format(result=temp[i],num=ans[i]))
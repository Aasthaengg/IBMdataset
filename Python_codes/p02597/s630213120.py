n = int(input())
c = input()

#右端から見ていって初めのRが出たらWとRをカウントする
cnt = 0
R = 0
W = 0

for i in range(n):
    if c[i] == "R":R += 1
    else:W += 1

for i in range(R):
    if c[i] == "W":cnt += 1
print(cnt)
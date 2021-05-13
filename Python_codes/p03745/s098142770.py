import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
a_ = []
for i in a:
    if not a_:
        a_.append(i)
    elif i != a_[-1]:
        a_.append(i)
cnt = 0
flag = 0
for i in range(len(a_) - 1):
    if flag == 0:
        if a_[i + 1] - a_[i] > 0:
            flag = 1
        else:
            flag = -1
        continue
    if flag == 1 and a_[i + 1] - a_[i] < 0:
        cnt += 1
        flag = 0
    elif flag == -1 and a_[i + 1] - a_[i] > 0:
        cnt += 1
        flag = 0
print(cnt + 1)

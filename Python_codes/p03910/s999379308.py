import sys

N = int(sys.stdin.readline().strip())

A = []
t = 0
i = 1
while t <= N:
    t += i
    A.append(i)
    i += 1
# print(A) 
for i in A:
    if t - N == i:
        # print("continue", i)
        continue
    else:
        print(i)
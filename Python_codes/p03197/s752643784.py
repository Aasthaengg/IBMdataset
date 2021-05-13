from sys import stdin, stdout
import bisect

n = int(stdin.readline().strip())
flag = 0
for i in range(n):
    tmp = int(stdin.readline().strip())
    if tmp % 2:
        flag = 1
        break
if flag:
    stdout.writelines('first\n')
else:
    stdout.writelines('second\n')
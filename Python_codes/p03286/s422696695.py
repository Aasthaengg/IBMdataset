from math import floor
n = int(input())
s = ""
if n == 0:
    print(0)
    exit()
while n:
    s += str(n%2)
    n = n//2
    n *= (-1)
    # print(n)
    # if n == -1:
    #     break
print(s[::-1])
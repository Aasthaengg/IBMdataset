n = int(input())
s = input()
t = input()
if s == t:
    ret = n
else:
    ret=2*n
    for i in range(1, n):
       if s[i:] == t[:-i]:
            ret = n + i
            break   



print(ret)
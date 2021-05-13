n = int(input())
s = {"AC":0,"WA":1,"TLE":2,"RE":3}
d=[0]*4
for i in range(n):
    d[s[input()]] += 1
for key in s.keys():
    print(key,"x",d[s[key]])
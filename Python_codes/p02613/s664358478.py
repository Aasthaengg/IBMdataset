
n = int(input())

d = {"AC":0,"WA":0,"TLE":0,"RE":0}
for _ in range(n):
    st = input()
    d[st] += 1

for x,y in d.items():
    print(x,"x",y)




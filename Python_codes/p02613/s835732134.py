manage = {"AC":0,"WA":0,"TLE":0,"RE":0}
N = int(input())
for i in range(N):
    manage[str(input())] += 1

for k,v in manage.items():
    print(str(k) + " x " + str(v))


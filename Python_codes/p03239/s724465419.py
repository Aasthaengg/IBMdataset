n, t = map(int, input().split())

data = []

for i in range(n):
    tmp = input().split()
    tmp[0] = int(tmp[0])
    tmp[1] = int(tmp[1])
    data.append(tmp)

data.sort()


flg = False
for i in range(len(data)):
    if data[i][1] <= t:
        print(data[i][0])
        flg = True
        break

if not flg:
    print("TLE")
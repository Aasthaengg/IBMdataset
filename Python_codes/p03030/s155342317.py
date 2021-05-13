n = int(input())
sp = []
for i in range(n):
    city, point = input().split()
    sp.append([city, int(point), int(i+1)])

sp.sort(key=lambda x: x[1], reverse=True)
sp.sort(key=lambda x: x[0])
for i in sp:
    print(i[2])

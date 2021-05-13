from sys import stdin
data = stdin.readlines()

N = int(data[0])
l = [0, 0]
i = 1
while i <= N:
    l.append(int(data[i].split()[0]))
    l.append(int(data[i].split()[1])+int(data[i].split()[2]))
    i += 1

def check(x):
    diffrent_time = l[2*x] - l[2*x-2]
    diffrent_place = abs(l[2*x+1] - l[2*x-1])
    return diffrent_time % 2 == diffrent_place % 2 and diffrent_time >= diffrent_place

count = 0
i = 1
while i <= N:
    if check(i) == False:
        count = 1
    i += 1
if count == 0:
    print("Yes")
elif count == 1:
    print("No")
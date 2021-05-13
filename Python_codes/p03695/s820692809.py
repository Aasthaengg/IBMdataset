import sys,collections
input = sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))
count = [0]*9
for ai in a:
    if 1 <= ai < 400:
        count[0] = 1
    elif 400 <= ai < 800:
        count[1] = 1
    elif 800 <= ai < 1200:
        count[2] = 1
    elif 1200 <= ai < 1600:
        count[3] = 1
    elif 1600 <= ai < 2000:
        count[4] = 1
    elif 2000 <= ai < 2400:
        count[5] = 1
    elif 2400 <= ai < 2800:
        count[6] = 1
    elif 2800 <= ai < 3200:
        count[7] = 1
    else:
        count[8] += 1
print(max(1,sum(count[:-1])),sum(count))

n = int(input())
ls = [0]*n
for i in map(int, input().split()):
    ls[i-1] += 1
for j in ls:
    print(j)
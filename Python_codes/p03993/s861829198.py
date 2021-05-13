from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
n = int(stdin.readline().rstrip())
li = list(map(int,stdin.readline().rstrip().split()))
point = 1
for i,j in enumerate(li):
    if li[j-1] == i+1:
        point += 1
point //= 2
print(point)
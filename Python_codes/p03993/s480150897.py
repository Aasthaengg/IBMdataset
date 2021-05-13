from sys import stdin

n = int(stdin.readline().rstrip())
li = [1]+list(map(int,stdin.readline().rstrip().split()))
point = 0
for i in range(1,n+1):
    if li[li[i]] == i:
        point += 1
print(point//2)
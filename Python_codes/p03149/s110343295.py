from sys import stdin

li = list(map(int,stdin.readline().rstrip().split()))
li.sort()

if li == [1,4,7,9]:
    print("YES")
else:
    print("NO")
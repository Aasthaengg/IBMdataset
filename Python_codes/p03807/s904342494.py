from sys import stdin

n = int(stdin.readline().rstrip())
li = list(map(int,stdin.readline().rstrip().split()))
count = 0
for i in li:
    if i%2 == 1:
        count += 1
if count %2 == 1:
    print("NO")
else:
    print("YES")

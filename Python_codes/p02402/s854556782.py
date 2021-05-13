count = int(input())
alist = [int(i) for i in input().split()]
minol = min(alist)
maxol = max(alist)
total = 0
for x in alist :
    total += x
print(minol,maxol,total)
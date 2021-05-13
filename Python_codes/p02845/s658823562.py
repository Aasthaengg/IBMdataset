import sys
l = [0] * 3
n = int(input())
a = [int(i) for i in input().split()]
m = 1000000007
ans = 1
for i in a:
    if(l.count(i) == 3):
        ans = ans * 3 % m
        l[0] += 1
    elif(l.count(i) == 2):
        ans = ans * 2 % m
        l = [i+1, i, sum(l)-2*i]
    elif(l.count(i) == 1):
        l[l.index(i)] += 1
    else:
        print(0)
        sys.exit()

print(ans)
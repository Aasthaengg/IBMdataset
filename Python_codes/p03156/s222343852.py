from sys import stdin

n = int(stdin.readline().rstrip())
a,b = [int(x) for x in stdin.readline().rstrip().split()]
li = list(map(int,stdin.readline().rstrip().split()))

one = 0
two = 0
three = 0

for i in li:
    if i <= a:
        one += 1
    elif a+1 <= i <= b:
        two += 1
    else:
        three += 1
print(min(one,two,three))
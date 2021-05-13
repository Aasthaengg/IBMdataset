from sys import stdin
n = int(stdin.readline().rstrip())
li = [stdin.readline().rstrip() for _ in range(n)]
b_sta = 0
a_last = 0
b_a = 0
ab = 0
for i in li:
    ab += i.count("AB")
    if i[0] == "B" and i[-1] == "A":
        b_a += 1
    elif i[0] == "B":
        b_sta += 1
    elif i[-1] == "A":
        a_last += 1
if b_a == 0:
    print(ab+min(a_last,b_sta))
else:
    if a_last + b_sta > 0:
        print(ab+b_a+min(a_last,b_sta))
    else:
        print(ab+b_a-1)
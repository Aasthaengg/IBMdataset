s = list(input())
w = int(input())
l = []
for i in range(len(s)):
    if i % w == 0:
        l.append(s[i])
for x in l:
    print(x,end="")
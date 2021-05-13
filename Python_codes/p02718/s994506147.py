a, b = map(int, input().split())
c = list(map(int, input().split()[:a]))
c.sort(reverse = True)
d = c[:b]
e = 0
for i in d:
    if i >= ((1/(4*b))*sum(c)):
        e += 1
if e==b:
    print("Yes")
else:
    print("No")
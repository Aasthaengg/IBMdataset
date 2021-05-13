N = int(input().strip())
s = 0
for i in input().strip().split(" "):
    s += int(i)%2
if s % 2 == 0:
    print("YES")
else:
    print("NO")

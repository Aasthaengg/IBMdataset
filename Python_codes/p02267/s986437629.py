n = int(input())
s = input().split()
m = int(input())
t = input().split()
c = 0
for i in t:
    if i in s:
        c += 1
print(c)

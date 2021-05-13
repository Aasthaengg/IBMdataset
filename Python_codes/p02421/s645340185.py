a = 0
b = 0
num = int(input())
for i in range(num):
    s1,s2 = input().split()
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 < s2:
        b += 3
    elif s1 > s2:
        a += 3
    else:
        a += 1
        b += 1
print(a,b)


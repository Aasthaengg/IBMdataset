a = 0
for i in range(int(input())):
    s = input().split()
    a += (int(s[1]) - int(s[0]) + 1)
print(a)
s = list(map(int, input().split()))
x = s[2]-s[0]
y = s[3]-s[1]
l = [s[2]-y, s[3]+x, s[0]-y, s[1]+x]
for i in l:
    print(i)
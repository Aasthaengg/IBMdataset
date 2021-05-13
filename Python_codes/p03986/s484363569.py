x = input()
ans = c = 0
for i in x:
    if i=='S':
        c += 1
    else:
        if c>0:
            ans += 1
            c -= 1
print(len(x)-ans*2)
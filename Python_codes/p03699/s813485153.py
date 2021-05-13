n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
s.sort()
m = sum(s)
if m % 10 != 0:
    print(m)
else:
    for i in range(n):
        if (m-s[i]) % 10 != 0:
            print(m-s[i])
            break
    else:
        print(0)
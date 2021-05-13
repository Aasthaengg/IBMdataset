s = list(map(int, list(input())))
k = int(input())

f = True
for i in range(k):
    if s[i] == 1:
        continue
    else:
        print(s[i])
        f = False
        break
if f:
    print(1)

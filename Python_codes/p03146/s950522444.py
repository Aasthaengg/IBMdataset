s = int(input())
a = [s]
for i in range(1, 1000001):
    s = s//2 if s%2 == 0 else 3*s+1
    if s in a:
        print(i+1)
        break
    else:
        a.append(s)
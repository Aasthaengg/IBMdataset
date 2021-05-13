n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
square = []
s1= a[0]
c = 0
result = 0
for i in range(1, n):
    s2 = a[i]
    if s1 == s2:
        c += 1
        if c % 2 == 1:
            square.append(s1)
            if len(square) == 2:
                result = square[0] * square[1]
                break
    else:
        s1 = a[i]
        c = 0
print(result)
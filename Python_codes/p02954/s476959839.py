s = input()
def x(n):
    return n//2 + n%2
s= s+'R'
a = 'R'
ren =1
m = len(s)
ls = [0] * m
for i in range(1, m):
    b = s[i]
    if a == b:
        ren += 1

    else:
        if b == 'L':
            ls[i] +=ren-x(ren)
            ls[i-1] +=x(ren)
        else:
            ls[i-ren] +=x(ren)
            ls[i-ren-1] +=ren-x(ren)
        a = b
        ren = 1
print(*ls[:-1])
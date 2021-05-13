a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
T = [a, b, c, d, e]
for t in T:
    if t - a > k or e -t > k:
        print(':(')
        exit(0)
print('Yay!')

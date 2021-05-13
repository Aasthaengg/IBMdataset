x = int(input())

p5 = []
m = 1000
for i in range(-m, m+1):
    p5.append(i**5)

for ci in range(2*m+1):
    if p5[ci] - x in p5:
        a = [ci-m, p5.index(p5[ci] - x)-m]
        break
a = [str(i) for i in a]
print(' '.join(a))
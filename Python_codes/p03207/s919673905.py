n = int(input())
p = [0]*n
for i in range(n):
    p[i] = int(input())
p = sorted(p,reverse = True)
print(sum(p[1:])+p[0]//2)
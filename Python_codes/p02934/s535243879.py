n = int(input())
a = list(map(int,input().split()))

p = 1
for i in a:
    p *= i

b = []
for i in a:
    b.append(p//i)
print(p/sum(b))
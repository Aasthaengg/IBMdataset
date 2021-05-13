n,m,x = map(int,input().split())
r_list = [0 for i in range(n+1)]
a_list = list(map(int,input().split()))

for i in a_list:
    r_list[i] = 1

zahyo = x
a = 0

while zahyo != 0:
    zahyo -= 1
    if r_list[zahyo] == 1:
        a += 1
zahyo = x
b = 0

while zahyo != n:
    zahyo += 1
    if r_list[zahyo] == 1:
        b += 1

print(min(a,b))

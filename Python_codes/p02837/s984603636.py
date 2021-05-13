from itertools import product
N = int(input())
A = []
shougen = []
for i in range(N):
    a = int(input())
    A.append(a)
    ls = []
    for j in range(a):
        ls.append([int(k) for k in input().split()])
    shougen.append(ls)
truth = [0, 1]
ans = 0
for x in product(truth, repeat=N):
    num = 0
    for i, y in enumerate(x):
        if y == 1:
            for z in shougen[i]: 
                if x[z[0]-1] != z[1]:
                    num += 1
    if num == 0:
        ans = max(ans, sum(x))
print(ans)
n1, n2 = [int(i) for i in input().split()]

n3 = [int(j) for j in input().split()]

n3.sort(reverse=True)

n4 = 0
for i1 in range(n1):
    if i1 >= n2:
        n4 += n3[i1]
print(n4)
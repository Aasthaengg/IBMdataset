
r,c = tuple([int(x) for x in raw_input().split(" ")])

A = []

for i in range(r):
    A.append([int(x) for x in raw_input().split(" ")])

for lst in A:
    lst.append(sum(lst))
    print(" ".join([str(x) for x in lst]))

lst2=[0 for x in range(c)]
for i in range(c):
   for j in range(r):
       lst2[i] += A[j][i]

lst2.append(sum(lst2))
print " ".join([str(x) for x in lst2])
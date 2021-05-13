from sys import stdin
X,Y,Z,K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [int(x) for x in stdin.readline().rstrip().split()]
C = [int(x) for x in stdin.readline().rstrip().split()]

AB = []
for a in A:
    for b in B:
        AB.append(a+b)
        
AB.sort(reverse=True)
C.sort(reverse=True)
ABC = []

for ab in AB[:K]:
    for c in C[:K]:
        ABC.append(ab+c)
        
ABC.sort(reverse=True)

for abc in ABC[:K]:
    print(abc)
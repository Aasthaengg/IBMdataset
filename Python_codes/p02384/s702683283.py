A,B,C = (0,1,5,4),(1,2,4,3),(2,0,3,5)
D = (-1,3)

f = input().split()

for i in range(int(input())):
    t, s = map(f.index, input().split())
    if t in A and s in A:
        print(f[2]) if A.index(t) - A.index(s) in D else print(f[3])
    if t in B and s in B:
        print(f[0]) if B.index(t) - B.index(s) in D else print(f[5])
    if t in C and s in C:
        print(f[1]) if C.index(t) - C.index(s) in D else print(f[4])
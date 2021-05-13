d=input().split()
for _ in range(int(input())):
 t,f=[int(d.index(s))for s in input().split()]
 n=[(1,2,4,3,1),(0,3,5,2,0),(0,1,5,4,0),(1,0,4,5,1),(0,2,5,3,0),(1,3,4,2,1)][t]
 print(d[n[n.index(f)+1]])

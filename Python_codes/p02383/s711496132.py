op = {'N':(1,5,2,3,0,4), 'S':(4,0,2,3,5,1), 'E':(3,1,0,5,4,2), 'W':(2,1,5,0,4,3)}
f = input().split()
for i in input():
    f = [f[j] for j in op[i]]
print(f[0])
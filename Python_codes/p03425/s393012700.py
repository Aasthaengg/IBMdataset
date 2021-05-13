#M=0 A=1 R=2 C=3 H=4
p = [0,0,0,0,0,0,1,1,1,2]
q = [1,1,1,2,2,3,2,2,3,3]
r = [2,3,4,3,4,4,3,4,4,4]

n = int(input())
name = [0,0,0,0,0]
for i in range(n):
    s = input()
    if s[0] == 'M':
        name[0] += 1
    elif s[0] == 'A':
        name[1] += 1
    elif s[0] == 'R':
        name[2] += 1
    elif s[0] == 'C':
        name[3] += 1
    elif s[0] == 'H':
        name[4] += 1

ans = 0
for i in range(10):
    ans += name[p[i]] * name[q[i]] * name[r[i]]

print(ans)
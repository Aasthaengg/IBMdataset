import itertools

n = int(input())
m = 0
a = 0
r = 0
c = 0
h = 0
d = []
for i in range(5):
    d.append(i)
p_list = list(itertools.combinations(d, 3))

for i in range(n):
    name = input()
    if name[0] == 'M':
        m +=1
    elif name[0] == 'A':
        a +=1
    elif name[0] == 'R':
        r +=1
    elif name[0] == 'C':
        c +=1
    elif name[0] == 'H':
        h +=1
con = [m,a,r,c,h]
ans = 0
for i in range(len(p_list)):
    ans += con[p_list[i][0]] * con[p_list[i][1]] * con[p_list[i][2]]
    
print(ans)
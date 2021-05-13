n = int(input())
l = [input().split() for i in range(n)]
m = []

for i in l:
    m.append(int(i[0]))
    
max_a = max(m)
a_num = m.index(max_a)

b = int(l[a_num][1])
print(max_a + b)
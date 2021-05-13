n = int(input())
s = list()
t = list()
ans = 0
for i in range(n) :
    addS,addT = input().split()
    s.append(addS)
    t.append(int(addT))
x = input()
for i in t :
    if t.index(i) > s.index(x) : 
        ans+=i
print(ans)


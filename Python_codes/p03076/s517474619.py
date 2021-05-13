from itertools import permutations

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
a = [a,b,c,d,e]

perms = list(permutations(a))
ans = float('inf')
for x in perms:
    cur = 0 
    x = list(x)
    for i in range(5):
        cur += x[i]
        temp = cur % 10
        if temp != 0 and i != 4:
            cur += (10 - temp)
    ans = min(ans,cur)
print(ans)



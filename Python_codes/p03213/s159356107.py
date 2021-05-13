from collections import Counter

def fctr1(n): 
    f = []
    for i in range(2,int(n**0.5)+2):
        while n%i == 0:
            n = n//i
            f.append(i)
    if n != 1:
        f.append(n)
    return f


n = int(input())

p_list = []
for i in range(1,n+1):
    p_list = p_list + fctr1(i)

pc = Counter(p_list).most_common()

#print(pc)

c74 = 0
c24 = 0
c14 = 0
c4 = 0
c2 = 0

for i in range(len(pc)):
    if pc[i][1] >= 74:
        c74 += 1
    if pc[i][1] >= 24:
        c24 += 1
    if pc[i][1] >= 14:
        c14 += 1
    if pc[i][1] >= 4:
        c4 += 1
    if pc[i][1] >= 2:
        c2 += 1

ans = c74 + c24*(c2-1) + c14*(c4-1) + c4*(c4-1)//2*(c2-2)

print(ans)

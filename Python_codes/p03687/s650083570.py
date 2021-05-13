import copy
s = input()
n = len(s)
l = []
c = [0]*26

for i in s:
    l.append(ord(i)-ord("a"))
    c[l[-1]] += 1

ans = 10**10

for i in range(26):
    if c[i]:
        count = 0
        l2 = copy.deepcopy(l)
        while (n-count)*i != sum(l2):
            count += 1
            nl = []
            for j in range(n-count):
                if l2[j] == i or l2[j+1] == i:
                    nl.append(i)
                else:
                    nl.append(1000)
            l2 = nl
        ans = min(ans,count)
print(ans)

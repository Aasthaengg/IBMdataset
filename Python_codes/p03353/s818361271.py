s = input()
k = int(input())

se = set()
for i in range(len(s)+1):
    for j in range(i,i+k+1):
        se.add(s[i:j])
se.remove('')
l = sorted(list(se))
print(l[k-1])
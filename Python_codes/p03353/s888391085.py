s = input()
k = int(input())

se = set()
for i in range(len(s)):
    for j in range(1,k+1):
        se.add(s[i:i+j])

li = list(se)
li.sort()
print(li[k-1])
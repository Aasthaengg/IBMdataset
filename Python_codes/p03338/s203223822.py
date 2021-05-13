n = int(input())
s = input()
li = []
for i in range(n-1):
    cnt = 0
    for j in set(list(s[:i+1])):
        if j in set(list(s[i+1:])):
            cnt +=1
    li += [cnt]
print(max(li))
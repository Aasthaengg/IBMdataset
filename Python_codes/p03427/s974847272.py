n = int(input())
s = str(n)
l = list(s)
for i in range(len(l)):
    l[i] = int(l[i])
print(max(sum(l), int(l[0])-1 + (len(l)-1)*9))

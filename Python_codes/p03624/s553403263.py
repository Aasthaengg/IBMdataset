d = list(input())
d.sort()

l = list("abcdefghijklmnopqrstuvwxyz")
l.remove(d[0])
for i in range(len(d)-1):
    if d[i+1] != d[i]:
        l.remove(d[i+1])
if len(l) == 0:
    print("None")
else:
    print(l[0])

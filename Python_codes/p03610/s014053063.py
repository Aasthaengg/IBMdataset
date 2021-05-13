s = input()
a = len(s)//2 + len(s) % 2
li = []
for i in range(a):
    li.append(s[i*2])
print("".join(li))
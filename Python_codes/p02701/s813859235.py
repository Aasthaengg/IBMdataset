n = int(input())
name=[]
for _ in range(n):
    s = str(input())
    name.append(s)

print(len(set(name)))
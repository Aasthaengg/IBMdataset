n = int(input())
s = input().split()
q = int(input())
t = input().split()
cont = 0
for i in t:
    for o in s:
        if i == o:
            cont +=1
            break

print(cont)
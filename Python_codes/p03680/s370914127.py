n = int(input())
a = []
for _ in range(n):
    a.append(int(input())-1)

j = 0
pointer = 0
b = False
for i in range(n):
    j += 1
    if a[pointer] == 1:
        b = True
        break
    else:
        pointer = a[pointer]

print(j) if b == True else print(-1)
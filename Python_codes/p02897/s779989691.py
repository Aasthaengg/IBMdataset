a = int(input())
b = 0
c = 0
for i in range(1, a+1):
    b += 1
    if i%2==1:
        c+=1
print(c/b)
n = list(input())
p = 0
for i in range(1,len(n)):
    if int(n[i]) != 9:
        p = 1
        break
print(int(n[0])- p + 9*(len(n)-1))
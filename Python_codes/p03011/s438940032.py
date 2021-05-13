li = input().split()
for i in range(len(li)):
    li[i] = int(li[i])

li.remove(max(li))

print(li[0]+li[1])
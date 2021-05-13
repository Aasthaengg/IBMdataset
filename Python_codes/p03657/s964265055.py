li = list(map(int,input().split()))
li.append(li[0]+li[1])
for i in range(3):
    if li[i] % 3 == 0:
        print("Possible")
        exit()
print("Impossible")

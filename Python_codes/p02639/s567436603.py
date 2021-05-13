list_sunuke = input().split()
list_m = []

for i in range(5):
    list_m.append(i+1)

for i in range(5):
    if int(list_sunuke[i]) != list_m[i]:
        print(list_m[i])
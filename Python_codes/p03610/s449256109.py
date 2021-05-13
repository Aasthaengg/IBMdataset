s = input()
list = [] 
answer = ""

for i, j in enumerate(s):
    if i % 2 == 0:
        list.append(j)
    else:
        pass

print("".join(list))
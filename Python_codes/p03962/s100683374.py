list = list(map(int,input().split()))

counter = 0

for i in range(len(list)):
    if list[i] in list[i+1:]:
        continue
    else:
        counter += 1

print(counter)

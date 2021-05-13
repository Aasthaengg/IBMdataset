line = list(input())
j = 0
for i in range(3):
    if line[j] == "1":
        line[j] = "9"
    else:
        line[j] = "1"
    j +=1
print(int(line[0] + line[1] + line[2]))
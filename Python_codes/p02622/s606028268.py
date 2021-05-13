string1 = input()
string2 = input()

count = 0

for i in range(len(string1)):
    if string1[i] != string2[i]:
        count += 1
print(count)

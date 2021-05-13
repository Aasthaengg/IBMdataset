n = int(input())
s = input()

count = 0
for i in range(n):
    if(s[i] == "R"):
        count += 1

count2 = 0
for i in range(count):
    if(s[i] == "W"):
        count2 += 1

print(count2)
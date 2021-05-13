n = int(input())
s = input()
count = 0

for i,_ in enumerate(s) :
    if s[i:i+3] == "ABC":
        count += 1

print(count)
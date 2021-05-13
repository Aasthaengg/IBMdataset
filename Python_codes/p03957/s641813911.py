val = input()
count = 0
for i in range(len(val)):
    if val[i] == "C":
        for n in range(i+1, len(val)):
            if val[n] == "F" and count == 0:
                print("Yes")
                count += 1
if count == 0:
    print("No")
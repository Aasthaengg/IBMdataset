n = input()
for i in range(2):
    if len(set(n[i:i+3])) == 1:
        print("Yes")
        break
else:
    print("No")
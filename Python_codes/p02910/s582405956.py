s = input()
odd = ["R", "U", "D"]
even = ["L", "U", "D"]

for i in range(len(s)):
    if i%2 == 0:
        if not s[i] in odd:
            print("No")
            exit(0)
    else:
        if not s[i] in even:
            print("No")
            exit(0)

print("Yes")
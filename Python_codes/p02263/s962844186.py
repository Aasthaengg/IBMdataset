calc = input().split(" ")

nums = []
subTotal = 0

for i in range(len(calc)):
    if calc[i].isdigit():
        nums.append(int(calc[i]))
    else:
        b = nums.pop()
        a = nums.pop()

        if calc[i] == "+":
            subTotal = a + b
        elif calc[i] == "-":
            subTotal = a - b
        elif calc[i] == "*":
            subTotal = a * b
        
        nums.append(subTotal)

print(" ".join(map(str,nums)))
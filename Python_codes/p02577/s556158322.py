N = input()

num = 0
for n in N:
    num = num + int(n)

print("Yes") if(num % 9 == 0) else print("No")

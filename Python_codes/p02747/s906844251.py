S = input()

for i in range(1,6) :
    hita = "hi" * i
    if hita == S :
        print("Yes")
        exit()

print("No")

n = input(); a = 0; b = 0; c = int(n[0])
for i in range(len(n)):
    if n[i] != "9":
        if a == 0: a += 1; b = i
        else: a += 1
if a == 0: print(9*len(n))
elif a == 1 and b == 0: print(c+9*(len(n)-1))
else: print(c-1+9*(len(n)-1))
n = input()
n = n.split(" ")
conta = 0
for num in range(int(n[0]), int(n[1])+1):
    if num % int(n[2]) == 0:
        conta += 1
print(conta)
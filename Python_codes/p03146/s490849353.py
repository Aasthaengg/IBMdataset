def collatz(num):
    if num % 2 == 0:
        return num // 2
    elif num % 2 == 1:
        return num * 3 + 1

n = int(input())
collatz_list = [n]

for i in range(10**6):
    n = collatz(n)
    if not n in collatz_list:
        collatz_list.append(n)
    else:
        print(i+2)
        break
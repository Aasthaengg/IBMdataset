nyuryoku = input()
lists = nyuryoku.split()

a = int(lists[0])
b = int(lists[1])

if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd")
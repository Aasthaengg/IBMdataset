
n = int(input())
if n == 0:
    print(0)
    exit()
bit = []
while n != 0:
    bit.append(-(-n % -2))
    n = -(-n // -2)

for i in range(len(bit) - 1, -1, -1):
    print(bit[i], end = "")
print()
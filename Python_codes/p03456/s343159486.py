a, b = input().split()

ab = int(a + b)
#print(ab)
for c in range(1, 1200):
    if c ** 2 == ab:
        print("Yes")
        break
else:
    print("No")
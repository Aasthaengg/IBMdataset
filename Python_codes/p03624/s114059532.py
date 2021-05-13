S = input()
L = [chr(i) for i in range(ord('a'), ord('z')+1)]

for l in L:
    if l not in S:
        print(l)
        exit(0)

print("None")
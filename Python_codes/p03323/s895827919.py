a, b = map(int, input().split())

e = 0
squ = 0
for i in range(0, 16, 2):
    #for j in range(b)
    #s[i] = 1
    #s[i+1] = 0
    e += 1
    squ += 1

if e>=a and squ>=b:
    print("Yay!")
else:
    print(":(")

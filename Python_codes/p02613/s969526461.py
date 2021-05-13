N = int(input())
a, b, c, d = 0, 0, 0, 0 

for i in range(N):
    i = input()
    if i == "AC":
        a += 1
    elif i == "WA":
        b += 1
    elif i == "TLE":
        c += 1   
    elif i == "RE":
        d += 1

print("AC x " + str(a))
print("WA x " + str(b))
print("TLE x " + str(c))
print("RE x " + str(d))

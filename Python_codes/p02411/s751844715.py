grades = []
lettergrade = []

while True:
    m, f, r = input().split()    
    m = int(m)
    f = int(f)
    r = int(r)
    if m == f == r == -1:
        break
    grades.append([m, f, r])

for x in grades:
    if x[0] == -1 or x[1] == -1 or (x[0] + x[1] >= 0 and x[0] + x[1] < 30):
        lettergrade.append('F')
    elif x[0] + x[1] >= 80:
        lettergrade.append('A')
    elif x[0] + x[1] >= 65 and x[0] + x[1] < 80:
        lettergrade.append('B')
    elif (x[0] + x[1] >= 50 and x[0] + x[1] < 65) or (x[2] >= 50):
        lettergrade.append('C')
    else:
        lettergrade.append('D')

print("\n".join(lettergrade))
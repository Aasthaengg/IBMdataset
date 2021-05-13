n = int(input())
j = [0,0,0,0]
for i in range(0,n):
    s = input()
    if s == "AC":
        j[0] += 1
    elif s == "WA":
        j[1] += 1
    elif s == "TLE":
        j[2] += 1
    elif s == "RE":
        j[3] += 1
print('AC x ' +  str(j[0]))
print('WA x ' +  str(j[1]))
print('TLE x ' +  str(j[2]))
print('RE x ' +  str(j[3]))
N = int(input())

a = list(input() for _ in range(N))

AC_counter = 0
WA_counter = 0
TLE_counter = 0
RE_counter = 0

for value in a:
    if value == "AC":
        AC_counter+=1
    if value == "WA":
        WA_counter+=1
    if value == "TLE":
        TLE_counter+=1
    if value == "RE":
        RE_counter+=1


print ("AC x " + str(AC_counter))
print ("WA x " + str(WA_counter))
print ("TLE x " + str(TLE_counter))
print ("RE x " + str(RE_counter))
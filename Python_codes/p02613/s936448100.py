n = int(input())
l = list()

ac = 0
wa = 0
tle = 0
re = 0

for i in range(n):
    l.append(str(input()))

for i in range(n):
    if l[i] == "AC":
        ac += 1
    elif l[i] == "WA":
        wa += 1
    elif l[i] == "TLE":
        tle += 1
    elif l[i] == "RE":
        re += 1

print ("AC x ",ac)
print ("WA x ",wa)
print ("TLE x ",tle)
print ("RE x ",re)

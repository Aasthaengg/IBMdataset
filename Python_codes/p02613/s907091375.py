N = int(input())
count_ac = 0
count_wa = 0
count_tle = 0
count_re = 0
for i in range(N):
    s = input()
    if s == "AC":
        count_ac += 1
    elif s == "WA":
        count_wa += 1
    elif s == "TLE":
        count_tle += 1
    elif s == "RE":
        count_re += 1

s1 = "AC x " + str(count_ac)
s2 = "WA x " + str(count_wa)
s3 = "TLE x " + str(count_tle)
s4 = "RE x " + str(count_re)

print(s1)
print(s2)
print(s3)
print(s4)

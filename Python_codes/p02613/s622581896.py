N = int(input())
array = [input() for i in range(N)]
count_AC = 0
count_TLE = 0
count_RE = 0
count_WA = 0
for i in array:
    if i == "AC":
        count_AC += 1
    elif i == "TLE":
        count_TLE += 1
    elif i == "RE":
        count_RE += 1
    elif i == "WA":
        count_WA += 1
print("AC x "+str(count_AC))
print("WA x "+str(count_WA))
print("TLE x "+str(count_TLE))
print("RE x "+str(count_RE))
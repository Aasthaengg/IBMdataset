s = int(input())
sec = min = hour = 0
sec = s%60
if s >= 60:
    min = int(s/60)
    if min >= 60:
        hour = int(min/60)
        min = min%60
print(str(hour) + ':' + str(min) + ':' + str(sec))


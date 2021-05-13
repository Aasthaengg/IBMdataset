s = int(input())
min = int(s/60)
sec = s%60
hour = int(min/60)
min = min%60
print("{0}:{1}:{2}".format(hour, min, sec))
all_sec = int(input())
s = all_sec % 60
all_min = all_sec // 60
m = all_min % 60
h = all_min // 60
# ???????????¨?????????
print("{0}:{1}:{2}".format(h, m, s))
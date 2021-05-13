TimeS = int(raw_input())
TimeM = TimeS / 60
sec = TimeS % 60
hou = TimeM / 60
min = TimeM % 60

print(str(hou)+ ":"+ str(min)+ ":"+ str(sec))
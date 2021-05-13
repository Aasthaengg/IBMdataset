s = input()
int_s = int(s)
hour = int_s//3600
hour_Surplus = int_s%3600
minute = hour_Surplus//60
sec = hour_Surplus%60

print(str(hour)+":"+str(minute)+":"+str(sec))

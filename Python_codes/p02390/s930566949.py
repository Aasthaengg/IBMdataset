s = int(raw_input())
h = s / 3600
tmp = s % 3600
m = tmp / 60
s = tmp %60
time = map(str,[h,m,s])
print time[0]+":"+time[1]+":"+time[2]
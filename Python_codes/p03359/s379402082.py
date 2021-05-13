import datetime
a, b = map(int, input().split())
d = datetime.datetime(2018, 1, 1)
count = 0
while d <= datetime.datetime(2018, a, b):
	if (d.strftime('%m') == d.strftime('%d')):
		count+=1
	d = d + datetime.timedelta(days=1)
print(count)
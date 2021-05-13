num = int(raw_input())
hour = num / (60 * 60)
minute = (num % (60 * 60)) / 60
second = num % 60

print str(hour) + ':' + str(minute) + ':' + str(second)
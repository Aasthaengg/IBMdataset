sec_in = int(input())

hour = int(sec_in / 3600)
minute = int((sec_in % 3600) / 60)
sec = int(sec_in % 60)

print('{0}:{1}:{2}'.format(hour,minute,sec))

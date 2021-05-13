second = int(input())

minute = int(second / 60)
second = int(second % 60)

hour = int(minute / 60)
minute = int(minute % 60)

print("{0}:{1}:{2}".format(hour , minute , second))
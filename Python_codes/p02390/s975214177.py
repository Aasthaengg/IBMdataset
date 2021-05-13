
val = int(raw_input())
hour = 0
minute = 0

while 59 < val:
  if 59 < val:
    minute += 1
  if 59 < minute:
    minute = 0
    hour += 1
  val -= 60

print("%d:%d:%d" % (hour, minute, val))
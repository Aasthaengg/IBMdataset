import sys

input_sec = sys.stdin.readline()

input_sec = int(input_sec)

hour = input_sec / 3600

minute = (input_sec % 3600) / 60

second = input_sec % 60

print "%d:%d:%d" % (hour, minute, second)
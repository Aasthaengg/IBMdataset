import sys
input_line = map(int, sys.stdin.readline().split())
perimeter = (input_line[0] + input_line[1]) * 2
area = input_line[0] * input_line[1]
print "%d %d" % (area, perimeter)
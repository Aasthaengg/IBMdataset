import sys
input = sys.stdin.readline

s = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(7 - s.index(input()[:-1]))
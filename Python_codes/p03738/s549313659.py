a = int(input())
b = int(input())
ret = ''
if( a > b):
    ret = 'GREATER'
elif( a < b):
    ret = 'LESS'
else:
    ret = 'EQUAL'

print(ret)
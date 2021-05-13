a = input()
b = input()
if len(a) > len(b):
    ans = 'GREATER'
elif len(b) > len(a):
    ans = 'LESS'
elif a > b:
    ans = 'GREATER'
elif b > a:
    ans = 'LESS'
else:
    ans = 'EQUAL'
print(ans)
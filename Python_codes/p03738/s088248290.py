a = input()
b = input()

if len(a) != len(b):
    ans = 'GREATER' if len(a)>len(b) else 'LESS'
elif a != b:
    ans = 'GREATER' if a > b else 'LESS'
else:
    ans = 'EQUAL'

print(ans)


a = input().replace(' ', '+')
print('error' if eval(a) >= 10 else eval(a))
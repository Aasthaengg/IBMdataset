s = input()
date = s.split('/')
print('Heisei') if int(date[1]) <= 4 else print('TBD')
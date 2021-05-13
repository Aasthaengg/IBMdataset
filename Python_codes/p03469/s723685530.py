import datetime

S = input()
S = datetime.datetime.strptime(S, '%Y/%m/%d')



a = int(S.year)

if a != 2018:
    S = S.replace(2018)
    
print(S.strftime('%Y/%m/%d'))
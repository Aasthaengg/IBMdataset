S=input()
days = 'SUN,MON,TUE,WED,THU,FRI,SAT'.split(',')

index = days.index(S)
print(7-index)
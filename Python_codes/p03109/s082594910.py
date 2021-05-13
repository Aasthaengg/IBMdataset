date = list(map(int,input().split('/')))
print('Heisei'if date[0]<=2019 and date[1]<=4 and date[2]<=30 else 'TBD')
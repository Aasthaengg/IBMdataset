from datetime import datetime as dt
S = input()
D = dt.strptime(S,'%Y/%m/%d')
H = dt.strptime('2019/04/30','%Y/%m/%d')
if D<=H: print('Heisei')
else: print('TBD')
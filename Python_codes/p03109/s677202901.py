from datetime import datetime
y,m,d=map(int,input().split('/'))
print(['Heisei','TBD'][datetime(y,m,d)>datetime(2019,4,30)])
import sys,datetime
input = sys.stdin.readline

y,m,d = list(map(int,input().split('/')))
print('Heisei' if datetime.datetime(y,m,d) <= datetime.datetime(2019,4,30) else ('TBD'))

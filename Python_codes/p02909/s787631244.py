import sys
def S(): return sys.stdin.readline().rstrip()


d = {'Sunny':'Cloudy','Cloudy':'Rainy','Rainy':'Sunny'}
print(d[S()])

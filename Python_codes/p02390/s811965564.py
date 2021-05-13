time=int(input())
h=int(time/3600)
m=int((time%3600)/60)
s=time%60
print('{}:{}:{}'.format(h,m,s))


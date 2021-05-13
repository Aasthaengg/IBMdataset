S = int(input())

h = S // 3600
m = S // 60 % 60
s = S % 60

#print(h+ ':' + m + ':' + s)
print('{0}:{1}:{2}'.format(h,m,s));
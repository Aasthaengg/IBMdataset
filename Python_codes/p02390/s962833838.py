#coding utf-8
S = int(input())
s = S % 60
m = ((S // 60) % 60)
h = (S // 60) // 60
print('{0}:{1}:{2}'.format(h,m,s))

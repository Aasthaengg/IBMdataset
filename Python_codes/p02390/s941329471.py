s = int(input())
m, s = s // 60, s % 60
h, m = m // 60, m % 60
print(':'.join(map(str, [h,m,s])))
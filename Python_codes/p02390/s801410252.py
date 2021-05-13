S = int(raw_input())
h = S/3600
m = S%3600/60
s = S%3600%60
h,m,s = map(str,(h,m,s))
print h+':'+m+':'+s 
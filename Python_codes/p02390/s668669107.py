a = input()
a = int(a)
s = a%60
m = (a-a%60)/60%60
h = (a-s-m*60)/3600
m = int(m)
h = int(h)
s=str(s)
m=str(m)
h=str(h)
print(h + ':'+m+':'+s)
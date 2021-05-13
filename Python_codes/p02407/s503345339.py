t = int(raw_input())
x = raw_input().split()
s = ''
for i in range(0,t):
    k = int(x[t - i - 1])
    if i == 0:
        s = str(k)
    else:
        s = s + ' ' + str(k)
        
print s
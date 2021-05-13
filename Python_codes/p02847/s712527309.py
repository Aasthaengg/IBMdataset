s=input()
t='SUN,MON,TUE,WED,THU,FRI,SAT'
m=t.split(",")
for i in range(len(m)):
    if(m[i]==s):
        print(7-i)

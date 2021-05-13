N=int(input())
count=0
if N//100000==1:
    count=90909
elif N//10000>0:
    count=N%10000+910+((N//10000)-1)*10000
elif N//1000>0:
    count=909
elif N//100>0:
    count=N%100+10+((N//100)-1)*100
elif N//10>0:
    count=9
else:
    count=N//1
print(count)
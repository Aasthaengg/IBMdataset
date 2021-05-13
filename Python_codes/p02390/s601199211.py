time = int(input())
sec = time%60
min = (time//60)%60
hour = (time//60)//60

print (str(hour)+":"+str(min)+":"+str(sec))



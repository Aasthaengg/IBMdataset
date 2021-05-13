N = input()
target_second=int(N)
hour=target_second//3600
minute=target_second//60-hour*60
second=target_second%60
print(str(hour)+":"+str(minute)+":"+str(second))

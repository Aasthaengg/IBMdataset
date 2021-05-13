start_hour,start_min,end_hour,end_min,study_min =  list(map(int, input().split()))
day_time = (end_hour * 60 + end_min) - (start_hour*60 + start_min)
able_time = day_time - study_min
print(able_time)
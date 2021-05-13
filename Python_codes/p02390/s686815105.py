raw_time = int(raw_input())
 
if 0 <= raw_time < 86400:
    hour = raw_time / 3600
    min = (raw_time - hour * 3600) / 60
    sec = (raw_time - hour * 3600 - min * 60)
    print("%d:%d:%d")%(hour, min, sec)
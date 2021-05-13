hour1,min1,hour2,min2,ben = map(int,input().split())
ans=(hour2-hour1)*60+min2-min1-ben
print(ans)
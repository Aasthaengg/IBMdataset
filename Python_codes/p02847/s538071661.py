week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
S = input()

ans = 7
for i in range(len(week)):
    if S == week[i]:
        ans -= i
        
print(ans)
n,c = map(int,input().split())
data = []
for i in range(n):
    x,v = map(int,input().split())
    data.append([x,c-x,v])

value_right = [data[0][2]]
for x,y,z in data[1:]:
    value_right.append(value_right[-1]+z)

value_left = [data[n-1][2]]
for x,y,z in data[::-1][1:]:
    value_left.append(value_left[-1]+z)
value_left = value_left[::-1]

opt_right = []
now_opt = 0
for i in range(n):
    next_opt = max(now_opt,value_right[i]-data[i][0])
    opt_right.append(next_opt)
    now_opt = next_opt

#print(opt_right)
opt_left = []
now_opt = 0
for i in range(n-1,-1,-1):
    next_opt = max(now_opt,value_left[i]-data[i][1])
    opt_left.append(next_opt)
    now_opt = next_opt

#print(opt_left)

ans = 0
for turn in range(n):
    now = -data[turn][0] + value_right[turn]
    #print(now)
    ans = max(ans,now)
    now -= data[turn][0]
    if turn < n-1:
        #print(now + opt_left[n-2-turn])
        ans = max(ans,now + opt_left[n-2-turn])

for turn in range(n-1,-1,-1):
    now = -data[turn][1] + value_left[turn]
    #print(now)
    ans = max(ans,now)
    now -= data[turn][1]
    if turn > 0:
        #print(now + opt_right[turn-1])
        ans = max(ans,now + opt_right[turn-1])

print(ans)
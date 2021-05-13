D = int(input())
c_list = list(map(int,input().split(' ')))
s_list = []
for i in range(D):
    s_list.append(list(map(int,input().split(' '))))
t_list = []
for j in range(D):
    t_list.append(int(input()))
last_list = [0 for k in range(26)]
score = 0
point = 0
for day in range(D):
    point += s_list[day][t_list[day]-1]
    last_list[t_list[day]-1] = day+1
    for c in range(26):
        point -= c_list[c]*((day+1)-last_list[c])
    if(point>-1000000):
        score = point+1000000
    print(point)

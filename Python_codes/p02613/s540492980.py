n = int(input())
si = [input() for _ in range(n)]
ans_str = ['AC x', 'WA x', 'TLE x', 'RE x']
ans = [0]*4
for i in range(n):
    if si[i] == 'AC':
        ans[0] += 1
    elif si[i] == 'WA':
        ans[1] += 1
    elif si[i] == 'TLE':
        ans[2] += 1
    elif si[i] == 'RE':
        ans[3] += 1
    
for i in range(4):
    print(ans_str[i], ans[i])

n = int(raw_input())
t,a = map(int, raw_input().split(' '))
his = map(int, raw_input().split(' '))
m = (+float('inf'),-1)
for i,hi in enumerate(his): m = min(m, (abs(t - hi * 0.006 - a),i+1))
print  m[1]
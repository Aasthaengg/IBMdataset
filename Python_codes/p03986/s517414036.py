import sys
input = sys.stdin.readline

S = input().rstrip()
s_cnt =0
t_cnt =0

for s in S:
    if s == 'S':
        s_cnt += 1
    else:
        if s_cnt >0:
            s_cnt -= 1
        else:
            t_cnt += 1
            
print(t_cnt + s_cnt)

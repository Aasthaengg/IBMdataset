# contest = 'agc013'
# problem = 'a'
# testcase = 3

# import sys
# import os
# current_path = os.getcwd().split('/')
# path = '/workspaces/atcoder_docker_sample/tmp/{}_{}/sample-{}.in'.format(
#     contest,problem,testcase
# )
# f = open(path, 'r')
# sys.stdin = f

n = int(input())
a = list(map(int,input().split()))

if(n<3):
    print(1)
    exit()

ans = 1
state = 0
now = a[0]
for ai in a[1:]:
    if(state==0):
        if(now == ai):
            state = 0
        elif(now > ai):
            state = -1
        else:
            state = 1
    elif(state==1):
        if(now > ai):
            state = 0
            ans += 1
    else:
        if(now < ai):
            state = 0
            ans += 1
    now = ai

print(ans)
import bisect
n,c,k = map(int,input().split())

t = [0 for _ in range(n)]

for i in range(n):
    t[i] = int(input())

t.sort()
cnt = 0
st = 0
while st < n:
    fire_time = t[st] + k
    wait_num = bisect.bisect_right(t,fire_time) - st

    if(wait_num <= c):
        st = wait_num + st
    else:
        st = st + c
    cnt += 1

print(cnt)

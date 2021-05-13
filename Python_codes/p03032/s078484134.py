import bisect

abcd = []
n, k = map(int, input().split()) 
v_list = list(map(int, input().split())) 

for a in range(0, k+1):
    for b in range(0, k+1-a):
        for c in range(0, k+1-a-b):
            d = k-a-b-c
            abcd.append([a,b,c,d])


ans = 0
for curr_abcd in abcd:
    a,b,c,d = curr_abcd
    cd = c+d
    if a + b >= n:
        have = sorted(v_list)
    else:
        have = sorted(v_list[0:a] + v_list[n-b:n]) 

    minus_cnt = bisect.bisect_right(have,0)
    have = have[ min(minus_cnt, cd) : ]
    curr_sum = sum(have) 
    ans = max(ans, curr_sum)

print(ans)
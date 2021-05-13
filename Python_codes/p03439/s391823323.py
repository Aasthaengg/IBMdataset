N = int(input())

print(0)
start_ans = input()
if start_ans == 'Vacant':
    quit()
end_ans = start_ans
start = 0
end = N
while True:
    mid = (start+end)//2
    print(mid)
    mid_ans = input()
    if mid_ans == 'Vacant':
        quit()
    if (mid-start)%2 == (start_ans == mid_ans):
        end = mid
        end_ans = mid_ans
    else:
        start = mid
        start_ans = mid_ans 
import copy
a,b,c = map(int,input().split())
cnt = 0
if (a % 2 == 1) or (b % 2 == 1) or (c % 2 == 1):
    print(0)
    exit()
while 1:
    cnt += 1 
    next_a = b // 2 +  c // 2
    next_b = a // 2 + c // 2
    next_c = a // 2 + b // 2
    if a == next_a and b == next_b and c == next_c:
        print(-1)
        break
    elif (next_a % 2 == 1) or (next_b % 2 == 1) or (next_c % 2 == 1):
        print(cnt)
        break
    a = copy.deepcopy(next_a)
    b = copy.deepcopy(next_b)
    c = copy.deepcopy(next_c)



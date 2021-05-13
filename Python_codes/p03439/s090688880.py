import sys


def solve(mid):
    print(mid)
    sys.stdout.flush()
    mid_state = input()
    if mid_state == "Vacant":
        print(mid)
        exit()
    if ok % 2 == mid % 2:
        if ok_state == mid_state:
            return True, mid_state
        else:
            return False, mid_state
    else:
        if ok_state == mid_state:
            return False, mid_state
        else:
            return True, mid_state

n = int(input())

print(0)
sys.stdout.flush()
ok = 0
ok_state = input()
if ok_state == "Vacant":
    print(0)
    exit()
    
print(n-1)
sys.stdout.flush()
ng = n-1
ng_state = input()
if ng_state == "Vacant":
    print(n-1)
    exit()


while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    judge, state = solve(mid)
    if judge:
        ok = mid
        ok_state = state
    else:
        ng = mid
        ng_state = state
print(ok)
exit()
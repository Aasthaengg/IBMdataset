import sys

def judge(x):
    print(x)
    sys.stdout.flush()
    ans = str(input())
    if ans == "0":
        exit()
    else:
        return ans



n = int(input())
left = 0
mid = n//2
right = n-1

l = judge(left)
m = judge(mid)
r = judge(right)

while True:
    if ((mid-left)%2 == 0 and l == m) or ((mid-right)%2 == 1 and r == m) or ((left-mid)%2 == 1 and l != m) or ((mid-right)% 2 == 0 and r != m):
        left = mid
        mid = (left + right)//2
        l = m
        m = judge(mid)
    else:
        right = mid
        mid = (left + right)//2
        r = m
        m = judge(mid)
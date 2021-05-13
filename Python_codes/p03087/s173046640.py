from bisect import bisect_left, bisect_right
n,q = map(int, input().split())
s = input()
lr = [list(map(int, input().split())) for _ in range(q)]

numbers = []
for i in range(n-1):
    if s[i]+s[i+1] == "AC":
        numbers.append(i+1)
for l,r in lr:
    x,y = bisect_left(numbers, l), bisect_right(numbers, r)
    if x==y: print(0)
    elif numbers[y-1]+1 <= r:print(y-x)
    else: print(y-x-1)
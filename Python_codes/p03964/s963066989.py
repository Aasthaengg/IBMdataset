n = int(input())
before = [0, 0]
for i in range(n):
    t, a = map(int, input().split())
    if t >= before[0] and a >= before[1]:
        before = [t, a]
    else:
        mul = max((before[0]-1)//t+1, (before[1]-1)//a+1)
        before = [t*mul, a*mul]

print(sum(before))
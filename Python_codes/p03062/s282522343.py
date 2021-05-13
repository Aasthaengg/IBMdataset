n = int(input())
alst = list(map(int, input().split()))
minus = 0
for num in alst:
    if num < 0:
        minus += 1

blst = [abs(num) for num in alst]
blst.sort()

if 0 in alst:
    print(sum(blst))
elif minus % 2 == 0:
    print(sum(blst))
else:
    print(sum(blst[1:]) - blst[0])
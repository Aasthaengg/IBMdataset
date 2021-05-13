n = int(input())
a = list(map(int, input().split()))
abs_a = list(map(abs, a))

count = 0
for x in a:
    if x == 0:
        print(sum(abs_a))
        exit()
    elif x < 0:
        count += 1
if count % 2 == 1:
    mins = min(abs_a)
    print(sum(abs_a) - 2 * mins)
else:
    print(sum(abs_a))

n = int(input())
apple = list(map(int, input().split()))
orange = list(map(int, input().split()))
count = 0

for i in range(n):
    if orange[i] >= apple[i]:
        a = orange[i] - apple[i]
        count += apple[i]
        if apple[i+1] >= a and a != 0:
            b = apple[i + 1] - a
            apple[i+1] = b
            count += a
        elif apple[i + 1] < a and a != 0:
            count += apple[i + 1]
            apple[i + 1] = 0
        else:
            pass
    else:
        count += orange[i]
        apple[i] = 0
print(count)
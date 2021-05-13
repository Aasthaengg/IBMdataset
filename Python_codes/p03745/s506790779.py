n = int(input())

a = [0] * n

a = list(map(int, input().split()))

last = 0
cnt = 1
increase_flag = None
first_flag = True
for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        if (increase_flag is None):
            increase_flag = True
        elif not (increase_flag):
            cnt += 1
            increase_flag = None
        else:
            continue
    elif a[i] > a[i + 1]:
        if (increase_flag is None):
            increase_flag = False
        elif not (increase_flag):
            continue
        else:
            cnt += 1
            increase_flag = None

print(cnt)

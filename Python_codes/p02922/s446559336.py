A, B = map(int, input().split())
count = 1
a_count = 0
while True:
    if count >= B:
        print(a_count)
        break
    else:
        count += (A - 1)
        a_count += 1

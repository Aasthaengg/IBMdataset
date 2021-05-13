A,B = map(int,input().split())
if B == 1:
    answer = 0
elif B<=A:
    answer = 1
else:
    tap = 2
    while True:
        if tap*A-tap+1 >= B:
            answer = tap
            break
        else:
            tap += 1
print(answer)
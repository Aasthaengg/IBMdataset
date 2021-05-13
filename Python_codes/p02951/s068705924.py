A, B, C = map(int, input().split())
container1 = A - B
container2 = C
answer = container2 - container1
if answer >= 0:
    print(answer)
else:
    print('0')

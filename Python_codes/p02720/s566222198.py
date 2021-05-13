from collections import deque

k = int(input())

num0 =[i for i in range(1,10)]
num = deque()
num = deque(num0)

if k < 10:
    print(k)
    
else:
    while True:
        x = num.popleft()
        if x % 10 != 0:
            num.append(10*x +(x % 10)-1)
            num0.append(10*x +(x % 10)-1)
            if len(num0) == k:
                break
        num.append(10*x +(x % 10))
        num0.append(10*x +(x % 10))
        if len(num0) == k:
            break
        if x % 10 != 9:
            num.append(10*x +(x % 10)+1)
            num0.append(10*x +(x % 10)+1)
            if len(num0)==k:
                break
    print(num0[-1])
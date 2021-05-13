from collections import deque
K = int(input())

q = deque([1,2,3,4,5,6,7,8,9])

for _ in range(K):
    x = q.popleft()
    ichi_no_kurai = x%10
    if ichi_no_kurai == 0:
        q.append(10*x+ichi_no_kurai)
        q.append(10*x+ichi_no_kurai+1)
    elif x%10 == 9:
        q.append(10*x+ichi_no_kurai-1)
        q.append(10*x+ichi_no_kurai)
    else:
        q.append(10*x+ichi_no_kurai-1)
        q.append(10*x+ichi_no_kurai)
        q.append(10*x+ichi_no_kurai+1)
print(x)
def checker(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0 :
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0 :
            return False
    return True

cnt=0
q=int(input())
for _ in range(q):
    v=int(input())
    if checker(v):
        cnt += 1
print(cnt)
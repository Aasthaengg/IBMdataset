ABC = list(map(int, input().split()))
cnt = 0
while len(set(ABC))!=1:
    A = sorted(ABC)[0]
    B = sorted(ABC)[1]
    C = sorted(ABC)[2]
    if ABC[0]%2==ABC[1]%2==ABC[2]%2:
        A += 2
        cnt += 1
    else:
        A += 1
        B += 1
        cnt += 1
    ABC = A,B,C
print(cnt)
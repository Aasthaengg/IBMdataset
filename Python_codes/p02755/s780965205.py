A, B = list(map(int, input().split()))

flag = False

for a in range(12, 1263):
    if flag:
        break
    for b in range(10, 1001):
        a_tax = int(a * 0.08)
        b_tax = int(b * 0.10)
        if(a_tax == A and b_tax == B and a == b):
            print(a)
            flag = True
            
else:
    print(-1)
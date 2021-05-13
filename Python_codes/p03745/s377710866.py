N = int(input().strip())
A = [int(i) for i in input().strip().split(" ")]

count = 1
prev = A[0]
up = False
down = False
for a in A[1:]:
    if prev < a:
        if up:
            count += 1
            up = False
        elif down:
            pass
        else: # 初回
            down = True
    elif prev > a:
        if up:
           pass
        elif down:
            count += 1
            down = False
        else: # 初回
            up = True
    else:
        pass
    prev = a

print(count)

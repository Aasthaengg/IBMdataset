A,B,C = map(int, input().split())

can_choose = True
work = C
while True:
    work += B
    work = work % A
    if work == 0:
        break
    elif work == (C % A):
        can_choose = False
        break

if can_choose:
    print("YES")
else:
    print("NO")
A, B = map(int, input().split())

p_lst = []
f = False
for p in range(1, 100*11):
    if int(p*0.08) == A and int(p*0.1) == B:
        p_lst.append(p)
        f = True
if not f:
    print(-1)
else:
    print(min(p_lst))
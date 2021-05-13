h,w, a, b = map(int, input().split())

current = [i for i in range(a)]
cnt = 0
for i in range(h):
    if i < b:
        s = [str(0) if i < a else str(1) for i in range(w)]
    else:
        s = [str(1) if i < a else str(0) for i in range(w)]
    print(''.join(s))

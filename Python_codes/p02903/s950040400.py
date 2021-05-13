h,w,a,b = map(int, input().split(' '))
result = []
if h < b or w < a:
    print(0)
else:
    for i in range(b):
        r = [0 if x < a else 1 for x in range(w)]
        result.append(r)
    for i in range(b, h):
        r = [1 if x < a else 0 for x in range(w)]
        result.append(r)
    for i in result:
        print(''.join(map(str, i)))
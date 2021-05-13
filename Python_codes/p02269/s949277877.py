n = int(input())
s = {2}
s.remove(2)
for i in range(n):
    order = list(map(str, input().split()))
    if (order[0][0] == 'i'):
        s.add(order[1])
    else:
        if order[1] in s:
            print('yes')
        else:
            print('no')
        

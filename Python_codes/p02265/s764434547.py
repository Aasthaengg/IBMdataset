from collections import deque

N=int(input())
array=deque()
for n in range(N):
    bun=input()
    if bun=='deleteFirst':
        del array[0]
    elif bun=='deleteLast':
        del array[-1]
    else:
        order,num=bun.split()
        if order=='insert':
            array.insert(0,num)
        else:
            try:array.remove(num)
            except:pass
print(' '.join(array))


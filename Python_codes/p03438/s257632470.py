N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if sum(a) > sum(b):
    print('No')
elif a == b:
    print('Yes')
elif sum(a) == sum(b):
    print('No')
else:
    count = 0
    diff = 0
    for ai,bi in zip(a,b):
        if ai == bi:
            continue
        elif ai < bi:
            diff += (bi-ai)//2
            continue
        else:
            count += (ai-bi)
    if diff >= count:
        print('Yes')
    else:
        print('No')
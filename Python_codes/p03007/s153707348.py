def c(n,a):
    a.sort()
    max = a.pop()
    min = a.pop(0)
    opr = []
    for i in a:
        if i >= 0:
            opr.append('{} {}'.format(min, i))
            min-=i
        else:
            opr.append('{} {}'.format(max, i))
            max-=i
    opr.append('{} {}'.format(max, min))
    return str(max - min) + '\n' + '\n'.join(opr)

n = int(input())
a = list(map(int, input().split()))
print(c(n, a))
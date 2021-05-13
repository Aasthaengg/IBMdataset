S = input()
K = int(input())

def count(s):
    """何文字変更が必要か
    """
    a = []
    b = ''
    c = 1
    for si in s:
        if b == si:
            c += 1
        else:
            a.append(c)
            c = 1
        b = si
    a.append(c)

    r = 0
    for ai in a:
        r += ai // 2
    # print(s, a, r)
    return r

if K == 1:
    ans = count(S)
elif len(S) == 1:
    ans = K // 2
elif len(set(S)) == 1:
    c = count(S*2)
    if K % 2 == 0:
        ans = c * (K//2)
    else:
        diff = count(S*3) - count(S*2)
        ans = c * (K//2) + diff
else:
    a1 = count(S*2)
    a2 = count(S*3)
    ans = a1 + (a2-a1) * (K-2)

print(ans)

# for i in range(1, 10):
#     print(i, S*i, count(S*i))

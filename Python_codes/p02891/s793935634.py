s = input()
k = int(input())
n = len(s)

def f(S):
    res = 0
    count = 1
    length = len(S)
    for i in range(1,length):
        if S[i] == S[i-1]:
            count += 1
        else:
            res += count // 2
            count = 1
    res += count // 2
    return res

res1 = f(s)
res2 = f(s+s)
res3 = f(s+s+s)

if res2 - res1 == res3 - res2:
    print(res1 + (res2-res1) * (k-1))
else:
    print(n * k // 2)

A, B, Q = map(int, input().split())
s = []
for _ in range(A):
    s.append(int(input()))
t = []
for _ in range(B):
    t.append(int(input()))
x = []
for _ in range(Q):
    x.append(int(input()))

def binsearch(threshold, lst):
    left, right = -1, len(lst)

    while right - left > 1:
        mid = (left + right) // 2
        if lst[mid] > threshold:
            right = mid
        else:
            left = mid
    return (left, right)

for q in x:
    ans = 10 ** 11
    for i in range(2):
        for j in range(2):
            a = binsearch(q, s)[i]
            b = binsearch(q, t)[j]
            #print(i, j, a, b)
            if 0 <= a <= A - 1 and 0 <= b <= B - 1:
                    #print(s[a], t[b], q)
                    ans = min(ans, abs(s[a] -t[b]) + min(abs(s[a]-q), abs(t[b]-q)))
    print(ans)
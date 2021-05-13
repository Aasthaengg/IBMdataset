def linear_search(arr, key):
    idx = 0
    while arr[idx] != key:
        idx += 1

    if idx == len(arr) - 1:
        return False

    return True


n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

s.append(None)
cnt = 0
for i in range(q):
    s[n] = t[i]
    if linear_search(s, t[i]):
        cnt += 1

print(cnt)


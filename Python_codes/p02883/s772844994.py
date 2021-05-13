def is_ok(a_list, f_list, score, k):
    cnt = 0
    for i in range(len(a_list)):
        target = score // f_list[i]
        cnt += max(0, a_list[i] - target)
        if cnt > k:
            return False
    return True


n, k = map(int, input().split())
a_list = list(map(int, input().split()))
f_list = list(map(int, input().split()))

a_list.sort()
f_list.sort()
f_list.reverse()

ok, ng = 10 ** 12, -1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(a_list, f_list, mid, k):
        ok = mid
    else:
        ng = mid
print(ok)

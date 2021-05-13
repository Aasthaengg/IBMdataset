n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_c = list(map(int, input().split()))
list_a.sort()
list_b.sort()
list_c.sort()
list_a.append(10**10)
list_b.append(10**10)
list_c.append(10**10)

list_memo = []
i = 0
j = 0
k = 0
start = 0
list_ans = []
a_count = 0
while k < n:
    if list_c[k] == min(list_a[i], list_b[j], list_c[k]):
        list_memo.append(0)
        list_memo[-1] = sum(list_memo[start:-1])
        list_ans.append(list_memo[-1])
        start = len(list_memo) - 1
        k += 1
    elif list_b[j] == min(list_a[i], list_b[j], list_c[k]):
        list_memo.append(a_count)
        j += 1
    else:
        list_memo.append(0)
        a_count += 1
        i += 1
print(sum(list_ans))

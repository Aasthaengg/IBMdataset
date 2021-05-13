n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
diff_po = []
diff_ne = []
if sum(a) < sum(b):
    print(-1)
else:
    ans = 0
    for i in range(n):
        if a[i] - b[i] < 0:
            diff_ne.append(a[i]-b[i])
        elif a[i] - b[i] > 0:
            diff_po.append(a[i]-b[i])
    diff_ne.sort(reverse = True)
    diff_po.sort()
    tmp_po = 0
    while len(diff_ne):
        tmp_ne = diff_ne.pop()
        ans += 1
        while tmp_ne < 0:
            if tmp_po <= 0:
                tmp_po = diff_po.pop()
                ans += 1
            #print(tmp_po,tmp_ne)
            if abs(tmp_po) > abs(tmp_ne):
                tmp_po += tmp_ne
                tmp_ne = 0
            else:
                tmp_ne += tmp_po
                tmp_po = 0
    print(ans)

n = int(input())
v = list(map(int, input().split()))

odd = {}
even = {}
for d, i in enumerate(v):
    if d % 2 == 1:
        if i in even:
            even[i] += 1
        else:
            even[i] = 1
    else:
        if i in odd:
            odd[i] += 1
        else:
            odd[i] = 1
even_sorted = sorted(even.items(), key=lambda x:x[1])
odd_sorted = sorted(odd.items(), key=lambda x:x[1])
if even_sorted[-1][0] == odd_sorted[-1][0]:
    try:
        second_o = odd_sorted[-2][1]
    except:
        second_o = 0
    try:
        second_e = even_sorted[-2][1]
    except:
        second_e = 0
    print(min(n- even_sorted[-1][1] -second_o, n- second_e -odd_sorted[-1][1] ))
else:
    print(n - max(even.values()) - max(odd.values()))
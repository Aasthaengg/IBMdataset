n = int(input())
v = tuple(map(int, input().split()))

if len(set(v)) == 1:
    print(len(v)//2)
else:
    from collections import Counter
    ve = v[0::2]
    vec = Counter(ve).most_common()
    most_even = vec[0]

    vo = v[1::2]
    voc = Counter(vo).most_common()
    most_odd = voc[0]

    if most_even[0] == most_odd[0]:
        o2 = voc[1][1]
        e2 = vec[1][1]
        ans = n - max(most_even[1] + o2,
                      e2 + most_odd[1])
    else:
        ans = n - most_even[1] - most_odd[1]
    print(ans)
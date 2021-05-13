from collections import Counter

n = int(input())
V = list(map(int,input().split()))

even = V[::2]
odd = V[1::2]

cnt_even = Counter(even).most_common()
cnt_odd = Counter(odd).most_common()

even_num = cnt_even[0][0]
odd_num = cnt_odd[0][0]

if even_num == odd_num:
    if len(cnt_even) == 1 and len(cnt_odd) == 1:
        ans = min(len(even),len(odd))
    elif len(cnt_even) == 1:#oddを変えるしかない
        ans = (len(even)-cnt_even[0][1]) + (len(odd)-cnt_odd[1][1])
    elif len(cnt_odd) == 1:
        ans = (len(even)-cnt_even[1][1]) + (len(odd)-cnt_odd[0][1])
    else:
        ans = min((len(even)-cnt_even[0][1]) + (len(odd)-cnt_odd[1][1]), (len(even)-cnt_even[1][1]) + (len(odd)-cnt_odd[0][1]))
else:
    ans_e = len(even) - cnt_even[0][1]
    ans_o = len(odd) - cnt_odd[0][1]
    ans = ans_e + ans_o

print(ans)
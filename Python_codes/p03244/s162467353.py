import collections

N = int(input())
v = list(map(int,input().split()))

even = v[0::2]
odd = v[1::2]

count_even = collections.Counter(even).most_common()
count_sort_even = sorted(count_even, key = lambda x: x[1])[::-1]

count_odd = collections.Counter(odd).most_common()
count_sort_odd = sorted(count_odd, key = lambda x: x[1])[::-1]

if count_sort_even[0][0] != count_sort_odd[0][0]:  ans = N - count_sort_even[0][1] - count_sort_odd[0][1]
    
else:
    if len(count_sort_even) == 1:
        if len(count_sort_odd) == 1:  ans = N // 2
        else:  ans = N - count_sort_even[0][1] - count_sort_odd[1][1]
    elif len(count_sort_odd) == 1:  ans = N - count_sort_even[1][1] - count_sort_odd[0][1]
    else:
        ans1 = N - count_sort_even[1][1] - count_sort_odd[0][1]
        ans2 = N - count_sort_even[0][1] - count_sort_odd[1][1] 
        ans = min(ans1, ans2)    
    
print(ans)
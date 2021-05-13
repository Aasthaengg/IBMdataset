n = int(input())
a = list(map(int,input().split()))

even = {}
odd = {}
for i in range(n):
    if i%2 == 0:
        if a[i] not in even:
            even[a[i]] = 1
        else:
            even[a[i]] += 1
    else:
        if a[i] not in odd:
            odd[a[i]] = 1
        else:
            odd[a[i]] += 1

sorted_even = sorted(even.items(), reverse=True, key=lambda x:x[1])
sorted_odd = sorted(odd.items(), reverse=True, key=lambda x:x[1])

if sorted_even[0][0] != sorted_odd[0][0]:
    print(n - sorted_even[0][1] - sorted_odd[0][1])
elif sorted_even[0][1] == sorted_odd[0][1]:#最頻値とその出現回数が等しい
    if len(sorted_even) == 1 and len(sorted_odd) == 1:
        print(n//2)
    elif len(sorted_even) == 1:
        print(n - sorted_even[0][1] - sorted_odd[1][1])
    elif len(sorted_odd) == 1:
        print(n - sorted_even[1][1] - sorted_odd[0][1])
    elif sorted_even[1][1] > sorted_odd[1][1]:
        print(n - sorted_even[1][1] - sorted_odd[0][1])
    elif sorted_even[1][1] < sorted_odd[1][1]:
        print(n - sorted_even[0][1] - sorted_odd[1][1])
    else:
        print(n - sorted_even[0][1] - sorted_odd[1][1])#2番目の最頻値とその出現回数も等しい
elif sorted_even[0][1] > sorted_odd[0][1]:
    print(n - sorted_even[0][1] - sorted_odd[1][1])
else:
    print(n - sorted_even[1][1] - sorted_odd[0][1])
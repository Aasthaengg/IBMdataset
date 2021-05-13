from collections import Counter
n = int(input())
a = list(map(int,input().split()))
a_counter = Counter(a)
a_counter_li = list(a_counter)
if sum(a) == 0:
    print("Yes")
elif len(a)%3 != 0:
    print("No")
elif len(a_counter) > 3 or len(a_counter) <= 1:
    print("No")
elif len(a_counter) == 3:
    if a_counter[a_counter_li[0]] == n // 3 and a_counter[a_counter_li[1]] == n // 3 and a_counter[a_counter_li[2]] == n // 3:
        if a_counter_li[0]^a_counter_li[1]^a_counter_li[2] == 0:
            print("Yes")
        else:
            print('No')
    else:
        print("No")
else:
    a_counter_li.sort()
    if a_counter_li[0] == 0 and a_counter[a_counter_li[0]] == n // 3:
        print("Yes")
    else:
        print("No")
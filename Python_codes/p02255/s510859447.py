n = int(input())
lst = map(int,raw_input().split())
for i in range(len(lst)):
    v = lst[i]
    j = i - 1
    while j >= 0 and lst[j] > v:
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = v
    print ' '.join(map(str, lst))
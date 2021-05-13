import string

h, w = map(int, input().split())
Alpha = [x for x in string.ascii_lowercase]
Alpha_count = {x:0 for x in Alpha}

for _ in range(h):
    A = str(input())
    for a in A:
        Alpha_count[a] += 1

odd_count = 0
two_count = 0
four_count = 0

for a in Alpha:
    if Alpha_count[a]%2 == 1:
        odd_count += 1
    if Alpha_count[a] == 2:
        two_count += 1
    else:
        four_count += int(Alpha_count[a] // 4)
        if Alpha_count[a] >= 6 and Alpha_count[a]% 4 == 2:
            two_count += 1

if odd_count >= 2:
    ans = 'No'
elif h%2 == 0 and w%2 == 0:
    if four_count == int(h/2)*int(w/2):
        ans = 'Yes'
    else:
        ans = 'No'
elif h%2 == 0 and w%2 != 0:
    need_four_count = int(h/2)*int((w-1)/2)
    need_two_count = int(h/2)
    if four_count < need_four_count:
        ans = 'No'
    elif four_count == need_four_count:
        if two_count == need_two_count:
            ans = 'Yes'
        else:
            ans = 'No'
    elif four_count > need_four_count:
        if need_two_count == 2*(four_count - need_four_count) + two_count:
            ans = 'Yes'
        else:
            ans = 'No'
elif h%2 != 0 and w%2 == 0:
    need_four_count = int(w/2)*int((h-1)/2)
    need_two_count = int(w/2)
    if four_count < need_four_count:
        ans = 'No'
    elif four_count == need_four_count:
        if two_count == need_two_count:
            ans = 'Yes'
        else:
            ans = 'No'
    elif four_count > need_four_count:
        if need_two_count == 2*(four_count - need_four_count) + two_count:
            ans = 'Yes'
        else:
            ans = 'No'
else:
    if odd_count != 1:
        ans = 'No'
    else:
        need_four_count = int((h-1)/2)*int((w-1)/2)
        need_two_count = int((h-1)/2)+int((w-1)/2)
        if four_count < need_four_count:
            ans = 'No'
        elif four_count == need_four_count:
            if two_count == need_two_count:
                ans = 'Yes'
            else:
                ans = 'No'
        elif four_count > need_four_count:
            if need_two_count == 2*(four_count - need_four_count) + two_count:
                ans = 'Yes'
            else:
                ans = 'No'

print(ans) 
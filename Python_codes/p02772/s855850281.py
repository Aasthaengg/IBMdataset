N = int(input())


num = list(map(int, input().split()))


ok_list = []
ng_list = []

for i in num:
    if i % 2 == 1:
        ok_list.append(i)

    elif i % 3 == 0 or i % 5 == 0:
        ok_list.append(i)

    else:
        ng_list.append(i)

if not ng_list:
    print("APPROVED")
else:
    print("DENIED")
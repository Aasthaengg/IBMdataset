n = int(input())
a = sorted([int(i) for i in input().split()], reverse=True)
allzero = True
element = {}
for i in a:
    if i != 0:
        allzero = False
    if i not in element.keys():
        element[i] = 0
    element[i] += 1
if allzero:
    print('Yes')
else:
    if n % 3 != 0:
        print('No')
    elif len(element) == 2:
        if 0 in element.keys() and element[0] == n//3:
            print('Yes')
        else:
            print('No')
    elif len(element) == 3:
        judge = 0
        for k, v in element.items():
            judge ^= k
            if v != n//3:
                print('No')
                break
        else:
            if judge == 0:
                print('Yes')
            else:
                print('No')
    else:
        print('No')
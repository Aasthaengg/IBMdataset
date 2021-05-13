N = int(input())
list_A = [int(x) for x in input().split()]

odd = 0
for A in list_A :
    if A%2 == 1 :
        odd += 1

if odd%2 == 0 :
    print("YES")
else :
    print("NO")

n = int(input())
a = [int(x) for x in input().split()]

a_odd = len([x for x in a if x % 2 != 0])
#a_eve = len([x for x in a if x % 2 == 0])

if a_odd % 2 == 0:
    print("YES")
else:
    print("NO")
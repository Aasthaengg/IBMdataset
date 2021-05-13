n = int(input())
li_a = list(map(int, input().split()))
c_kisuu = len([a for a in li_a if a % 2 != 0])

if c_kisuu % 2 != 0:
    print("NO")
else:
    print("YES")

N = int(input())
As = [int(a) for a in input().split()]

a_uniq = set(As)

if len(a_uniq) == N:
    print("YES")
else:
    print("NO")

N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)
if sum(L[1:]) > L[0]:
    print("Yes")
else:
    print("No")

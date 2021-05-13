a, b, c = map(int, input().split())

org = [a, b, c]
org.sort(reverse=True)

if org[0] == org[1] + org[2]:
    print("Yes")
else:
    print("No")
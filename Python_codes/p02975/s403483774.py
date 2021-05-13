n = int(input())
a = list(map(int, input().split()))

b = list(set(a))

if a.count(0) == n:
    print("Yes")
elif len(b) == 2 and a.count(0) == n / 3:
    print("Yes")
elif len(b) == 3 and b[0] ^ b[1] ^ b[2] == 0 and a.count(b[0]) == n / 3 and a.count(b[0]) == n / 3:
    print("Yes")
else:
    print("No")
        

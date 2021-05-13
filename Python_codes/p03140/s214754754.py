n = int(input())
A = input().rstrip()
B = input().rstrip()
C = input().rstrip()
ans = 0
for a, b, c in zip(A, B, C):
    if a != b and b != c and c != a:
        ans += 2
    elif (a != b and b !=c) or (b!= c and c != a) or (c != a and a != b):
        ans += 1
print(ans)
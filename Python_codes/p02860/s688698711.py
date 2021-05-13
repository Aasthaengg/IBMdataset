n = int(input())
s = input()
print("Yes" if s == s[:n//2] * 2 and n % 2 == 0 else "No")
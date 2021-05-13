A, B, C, D = map(int, input().split())
takahasi = C // B
aoki = A // D
if C % B != 0:
    takahasi += 1
if A % D  != 0:
    aoki += 1 
if takahasi > aoki:
    print("No")
else:
    print("Yes")
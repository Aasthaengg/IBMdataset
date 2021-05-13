N = input()
A = input()
B = input()
C = input()
cnt = 0
for a,b,c in zip(A,B,C):
    if a == b and b == c and b == a:
        continue
    elif a != b and b != c and c != a:
        cnt += 2
    elif a == b and b != c:
        cnt += 1
    elif b == c and c != a:
        cnt += 1
    elif c == a and a != b:
        cnt += 1
    
print(cnt)
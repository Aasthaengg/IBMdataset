a = int(input())
b = input()
c = a//2
if b[:c] == b[c:]:
    print("Yes")
else:
    print("No")
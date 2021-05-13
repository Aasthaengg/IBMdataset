A, B, C = input().split()
print("YES") if list(A)[-1] == list(B)[0] and list(B)[-1] == list(C)[0] else print("NO")

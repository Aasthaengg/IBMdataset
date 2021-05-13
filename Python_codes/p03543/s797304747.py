n = input()
tmp = n[0] == n[1] == n[2] or n[1] == n[2] == n[3]
print("Yes" if int(n) % 1111 == 0 or tmp else "No")
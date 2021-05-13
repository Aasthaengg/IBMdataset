n_str = input()
print("Yes" if sum([int(c) for c in n_str]) % 9 == 0 else "No")
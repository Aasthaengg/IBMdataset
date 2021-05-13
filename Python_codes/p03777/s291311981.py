a = input().split()
print(a[1] if a[0] == 'H' else ('D' if a[1] == 'H' else 'H'))
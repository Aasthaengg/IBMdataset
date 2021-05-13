a, b = list(map(str, input().split()))
print(b if a=='H' else ('H' if b=="D" else 'D'))
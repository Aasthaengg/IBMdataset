input()
A = [a for i, a in enumerate(input().split()) if i % 2 == 0 and int(a) % 2 == 1]

print(len(A))

A = int(input())
B = int(input())

print([i+1 for i in range(3) if i+1 != A and i+1 != B][0])
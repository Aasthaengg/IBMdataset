A,B =sorted(map(int,input().split()))
total = 0
total = total + B
total = total + max(A,B-1)

print(total)
A = [int(input()) for i in range(5)]
B = []
for a in A :
    if a % 10 != 0 :
        B.append(a - a % 10 + 10)
    else :
        B.append(a)
diff = [(b - a) for a, b in zip(A, B)]
print(sum(B)-max(diff))

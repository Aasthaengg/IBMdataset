N = int(input())

A = list(range(4, 101, 4))
B = list(range(7, 101, 7))

is_made = False

if N in A or N in B:
    is_made = True
else:
    for a in A:
        for b in B:
            if a+b > N:
                break
            elif a+b == N:
                is_made = True
                break

if is_made:
    print("Yes")
else:
    print("No")
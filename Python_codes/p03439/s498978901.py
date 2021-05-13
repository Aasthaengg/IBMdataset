N = int(input())

print(0, flush = True)
s = input()
if s == "Vacant": exit()
else:
    reference_state = s
    opposite_state = ("Male" if s == "Female" else "Female") 
    low, high = 0, N
    count = 1
    while count < 20:
        mid = (low + high)//2
        expected_state = (reference_state if mid % 2 == 0 else opposite_state)
        print(mid, flush = True)
        s = input()
        if s == "Vacant":
            break
        else:
            if s == expected_state: low = mid
            else: high = mid
            count += 1

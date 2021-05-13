S = list(input())
S = [int(s) for s in S]

K = int(input())

num_digit = 0

for s in S:
    if s == 1:
        num_digit += 1
    else:
        print(s)
        break
        
    if num_digit >= K:
        print(s)
        break
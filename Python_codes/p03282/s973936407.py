S = input()
K = int(input())
total = 0
for n in S:
    if n == "1":
        total += 1
        if total == K:
            print(1)
            break
    else:
        print(n)
        break
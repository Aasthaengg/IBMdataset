[print("YES" if x[0] + x[1] == x[2] else "NO") for x in [sorted([x * x for x in [int(i) for i in input().split(" ")]]) for _ in range(int(input()))]]
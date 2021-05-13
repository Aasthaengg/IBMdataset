inps = input().split()
if len(inps) < 3:
    print("Illegal input.")
else:
    count = 0
    start = int(inps[0])
    end = int(inps[1])
    target = int(inps[2])
    for i in range(start, end+1):
        if target % i == 0:
            count += 1

print(count)
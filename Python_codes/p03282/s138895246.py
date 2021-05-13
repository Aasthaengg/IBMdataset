S = input()
K = int(input())

for s in S:
    if K != 1 and s == '1':
        K -= 1
        continue
    else:
        print(s)
        break

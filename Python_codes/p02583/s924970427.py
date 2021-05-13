n = int(input())
l = [int(v) for v in input().split()]
pairs = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        for k in range(j + 1, len(l)):
            a = l[i]
            b = l[j]
            c = l[k]
            if a == b or b == c or c == a:
                continue
            else:
                if a + b <= c or b + c <= a or c + a <= b:
                    continue
                else:
                    pairs += 1
print(pairs)
N = int(input())

NSP = []
for n in range(1, N+1):
    s, p = input().split()
    NSP.append([n, s, int(p)])

# sortはstable。レコードの中に同じキーがある場合、もともとの順序が維持される
sorted_NSP = sorted(NSP, key=lambda x: x[2], reverse=True)
sorted_NSP = sorted(sorted_NSP, key=lambda x:x[1]) 
for nsp in sorted_NSP:
    print(nsp[0])


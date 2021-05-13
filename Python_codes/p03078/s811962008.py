x, y, z, k = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)
AB_pair = []
for a in A:
    for b in B:
        AB_pair.append(a + b)
AB_pair.sort(reverse=True)

ans = []
for total in AB_pair[:3001]:
    for c in C:
        ans.append(total + c)
ans.sort(reverse=True)
print(*ans[:k], sep="\n")

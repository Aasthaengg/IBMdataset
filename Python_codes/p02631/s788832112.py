N = int(input())
A = list(map(int,input().split()))

xor_all = 0

for a in A:
    xor_all ^= a

#print(bin(xor_all))

ans = []
for a in A:
    ans.append(str(xor_all^a))

print(' '.join(ans))
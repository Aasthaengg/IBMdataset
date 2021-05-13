input()
xors = [int(num) for num in input().strip().split(' ')]

totXor = xors[0]

for i in range(1, len(xors)): totXor ^= xors[i]

result = [totXor^xor  for xor in xors]

ans = "";
for result in result:
    ans += str(result)+ " "

print(ans.strip())

N = int(input())
A, B = [], []
for _ in range(N):
    ai, bi = map(int, input().split())
    A.append(ai)
    B.append(bi)
AB = sorted(list(zip(A, B)))

count = len(AB)

# 先頭
count += AB[0][0] - 1

for i in range(N - 1):
    # i と j の間に何人入れられるか
    if AB[i + 1][0] > AB[i][0] + 1:
        count += AB[i + 1][0] - AB[i][0] - 1

# 末尾 (0点以上なので)
count += AB[-1][1] - 0

print(count)
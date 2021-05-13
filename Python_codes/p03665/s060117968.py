import math
N, P = map(int, input().split())
A = list(map(int, input().split()))

# 全探索(奇数か偶数に全てを分ける)
evenL = []
oddL = []
for i in range(N):
    if (A[i] % 2 == 0):
        evenL.append(A[i])
    else:
        oddL.append(A[i])

even = len(evenL)
odd = len(oddL)

# 2で割った袋の枚数のあまりが1になるような組み合わせを数える
sum_odd = 0
numL = []
for i in range(odd):
    if ((i + 1) % 2 == 1):
        numL.append(i + 1)

for i in numL:
    sum_odd += (math.factorial(odd) //
                math.factorial(odd - i) // math.factorial(i))
# 全体から奇数になるような選び方を引いたら偶数になる選び方になる

# 2で割ったあまりが偶数こになる
numevenL = []
sum_even = 0
for i in range(odd):
    if ((i + 1) % 2 == 0):
        numevenL.append(i + 1)

for i in numevenL:
    sum_even += ((math.factorial(odd) //
                  math.factorial(odd - i) // math.factorial(i)))

if (P % 2 == 1):
    print(2 ** N - ((sum_even + 1) * (2 ** even)))
else:
    print((sum_even + 1) * (2 ** even))

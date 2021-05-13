#正解者以外のポイントを1減らすことと、全員のポイントを1減らしてから正解者のポイントだけ1増やすのは同じこと
from collections import Counter
n, k, q = map(int, input().split())
point = k - q
participant = [point] * n
answer = [int(input()) for _ in range(q)]
count_a = Counter(answer)


for key, value in count_a.items():
    participant[key-1] += value

for i in participant:
    if i > 0:
        print("Yes")
    else:
        print("No")
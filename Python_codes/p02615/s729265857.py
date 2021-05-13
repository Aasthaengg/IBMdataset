N = int(input())
A = [int(x) for x in input().split(" ")]

A.sort(reverse=True)
score = A[0]
count = 1
for a in A[1:]:
    if count == len(A) - 1:
        break
    if count == (len(A) - 2):
        score += a
        count += 1
        continue
    score += a * 2
    count += 2

print(score)

inputted = list(map(int, input().split()))
N = inputted[0]
R = inputted[1]

internal_rating = lambda R, K: max(R, R + 100 * (10 - K))

answer = internal_rating(R, N)

print(answer)

# Beginner
def getInnerRating(N, R):
    return R + (100 * (10 - min(10, N)))

N, R = map(int, input().split())
ans = getInnerRating(N, R)
print(ans)